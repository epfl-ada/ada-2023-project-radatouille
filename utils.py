from ast import literal_eval
import pandas as pd
import numpy as np
import json
from tqdm import tqdm
import itertools

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib_venn import venn3
import seaborn as sns
import networkx as nx

from scipy.stats import pearsonr

import statsmodels.api as sm
from statsmodels.tools.tools import pinv_extended
from statsmodels.stats.outliers_influence import variance_inflation_factor

from sklearn.model_selection import KFold
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score



def process_actors(df, movies_threshold=6):
    """
    Function to process the actors column of the dataset
    Parameters:
        df (DataFrame): The dataset to process
    Returns:
        df_actors (DataFrame): The processed dataset with the actors column exploded
    """

    # Keep actors that have at least movies_threshold movies
    df_actors = df.copy()
    actor_counts = df_actors['freebase_actor_id'].value_counts()
    actors_to_keep = actor_counts[actor_counts >= movies_threshold].index
    df_actors = df_actors[df_actors['freebase_actor_id'].isin(actors_to_keep)]

    # Remove nan values
    df_actors.dropna(subset=['actor_name'], inplace=True)

    return df_actors

def process_genres(df):
    """
    Function to process the genres column of the dataset
    Parameters:
        df (DataFrame): The dataset to process
    Returns:
        df_genres (DataFrame): The processed dataset with the genres column exploded
    """

    # Function to parse the genres column
    def parse_genres(genres_str):
        try:
            genres_dict = literal_eval(genres_str)
            return list(genres_dict.values())
        except:
            return []

    # Apply the function to the genres column
    df_genres = df.copy()
    df_genres['genres'] = df_genres['genres'].apply(parse_genres)

    # Explode the dataset so each genre gets its own row
    df_genres = df_genres.explode('genres')

    return df_genres

def process_countries(df):
    """
    Function to process the countries column of the dataset
    Parameters:
        df (DataFrame): The dataset to process
    Returns:
        df_countries (DataFrame): The processed dataset with the countries column exploded
    """

    # Parse the countries column
    def parse_countries(countries_str):
        try:
            countries_dict = literal_eval(countries_str)
            return list(countries_dict.values())
        except:
            return None
            
    df_countries = df.copy()

    # Apply the function to the countries column
    df_countries['countries'] = df_countries['countries'].apply(parse_countries)

    # Explode the dataset so each (country, movie) gets its own row
    df_countries = df_countries.explode('countries')

    return df_countries

def process_languages(df):
    """
    Function to process the languages column of the dataset. The goal is to extract the first language of each movie.

    Parameters:
        df (DataFrame): The dataset to process

    Returns:
        df_language (DataFrame): The processed dataset with the languages column exploded
    """
    df_language = df.copy()
    # Function to convert string to dictionary
    def string_to_dict(column_string):
        try:
            return literal_eval(column_string)
        except ValueError:
            return {}

    # Function to get the first value from a dictionary
    def get_first_value_from_dict(column_data):
        if isinstance(column_data, dict) and len(column_data) > 0:
            return next(iter(column_data.values()))
        return None

    # Convert string representations of dictionaries to actual dictionaries
    df_language['languages'] = df_language['languages'].apply(string_to_dict)
    # Extract the first value for language
    df_language['languages'] = df_language['languages'].apply(get_first_value_from_dict)
    
    return df_language

def process_tropes(df, characters_data):
    """
    Function to process the tropes column of the dataset. The goal is to add the tropes to the dataset.
    
    Parameters:
        df (DataFrame): The dataset to process
        characters_data (DataFrame): The characters dataset
    
    Returns:
        df_tropes (DataFrame): The processed dataset with the tropes column exploded
    """

    def extract_character(character):
        """
        Extracts character information from a dictionary.

        Parameters:
            character_dict (dict): A dictionary containing character details.

        Returns:
            tuple: A tuple with extracted character details.
        """

        character_dict = json.loads(character)
        character_name = character_dict.get("char", "Unknown")
        movie_title = character_dict.get("movie", "Unknown")
        freebase_actor_map_id = character_dict.get("id", "Unknown")
        actor_name = character_dict.get("actor", "Unknown")

        return character_name, movie_title, freebase_actor_map_id, actor_name

    # Apply the function to the tropes column
    df_tropes = df.copy()
    df_tropes[['character_name', 'movie_name', 'freebase_actor_map_id', 'actor_name']] = df_tropes['character'].apply(lambda x: extract_character(x)).apply(pd.Series)

    # Add freebase_id of movie from characters_data based on freebase_actor_map_id
    df_tropes = pd.merge(df_tropes, characters_data[['freebase_actor_map_id', 'freebase_id']], on='freebase_actor_map_id', how='left')

    # Drop nan values
    df_tropes.dropna(subset=['freebase_id'], inplace=True)
    df_tropes = df_tropes.reset_index(drop=True)

    return df_tropes


def hotencode(df, column, id_column, prefix='onehot'):
    """
    Function to one-hot encode a column of a dataset. The one-hot encoding allows to transform a categorical column into multiple binary columns.
    It's useful to use a categorical column as a feature in a regression model.

    Parameters:
        df (DataFrame): The dataset to process
        column (str): The column to one-hot encode
        id_column (str): The column to use as index
        prefix (str): The prefix to use for the new columns - by default 'onehot'

    Returns:
        one_hot_df (DataFrame): The one-hot encoded dataset
    """

    df_filtered = df[[id_column, column]]

    # Create a new dataframe with the one hot encoded columns
    one_hot_df = pd.get_dummies(df_filtered, columns=[column], prefix=prefix)
    
    one_hot_columns = list(filter(lambda x: x.startswith(prefix), one_hot_df.columns))

    # Group by id_column and aggregate using max to ensure values are 0 or 1
    one_hot_df = one_hot_df.groupby(id_column)[one_hot_columns].max().astype('int').reset_index()
    
    return one_hot_df, one_hot_columns

def perform_OLS(df, X_columns, y_column, regularization=None, alpha=1.0, print_results=True):
    """
    Function to perform an OLS (Ordinary Least Squares) regression model.

    Parameters: 
        df (DataFrame): The dataset to process
        X_columns (list): The list of features to use
        y_column (str): The target variable
        regularization (str): The regularization method to use - either 'l1' (Lasso) or 'l2' (Ridge)
        alpha (float): The regularization parameter
        print_results (bool): Whether to print the results or not

    Returns:
        fitted_model (regression model): The fitted regression model
    """
    
    # Create the model
    x = df[X_columns]
    y = df[y_column]
    X = sm.add_constant(x)
    model = sm.OLS(y, X)

    # Fit the model with regularization
    if regularization == 'l1':
        # Lasso
        results_fr = model.fit_regularized(method='elastic_net', L1_wt=1, alpha=alpha)
        pinv_wexog,_ = pinv_extended(model.wexog)
        normalized_cov_params = np.dot(pinv_wexog, np.transpose(pinv_wexog))
        fitted_model = sm.regression.linear_model.OLSResults(model, results_fr.params, normalized_cov_params)
    elif regularization == 'l2':
        # Ridge
        results_fr = model.fit_regularized(method='elastic_net', L1_wt=0, alpha=alpha)
        pinv_wexog,_ = pinv_extended(model.wexog)
        normalized_cov_params = np.dot(pinv_wexog, np.transpose(pinv_wexog))
        fitted_model = sm.regression.linear_model.OLSResults(model, results_fr.params, normalized_cov_params)
    else:
        # No regularization
        fitted_model = model.fit()

    # Print results
    if print_results:
        # For regularized models, we do not have a summary method
        display(fitted_model.summary().tables[0])
        display(fitted_model.summary().tables[2])

    return fitted_model

def study_OLS(
    df,
    X_columns,
    y_column,
    colname='col_name',
    regularization=None,
    alpha=1.0,
    threshold=0.05,
    print_results=True,
    plot_barplot=True,
    print_qq=False,
    print_baseline=True,
    map_columns_name=None,
    title=None,
    limit_tops=20
    ):
    """
    This function performs an OLS regression model on a dataset and returns the significant results. 
    The function also plots the QQ plot and the barplot of the significant results with the confidence interval.

    Parameters:
        df (DataFrame): The dataset to process
        X_columns (list): The list of features to use
        y_column (str): The target variable
        colname (str): The name of the column to use for the barplot
        regularization (str): The regularization method to use - either 'l1' (Lasso) or 'l2' (Ridge)
        alpha (float): The regularization parameter
        threshold (float): The threshold to use for check if a feature is significant (t-test)
        print_results (bool): Whether to print the results or not
        plot_barplot (bool): Whether to plot the barplot or not
        print_qq (bool): Whether to print the QQ plot or not
        print_baseline (bool): Whether to print the baseline comparison or not
        map_columns_name (function): A function to map the column names
        title (str): The title of the barplot
        limit_tops (int): The number of top and bottom features to display

    Returns:
        significant_results (DataFrame): The significant results
        significant_columns (list): The list of significant columns
    """

    # Perform OLS
    model = perform_OLS(df, X_columns, y_column, regularization=regularization, alpha=alpha)

    # Print baseline comparison
    if print_baseline:
        compare_baseline(model, df, X_columns, y_column, print_results=True)


    # Find and print results with p-values less than threshold
    significant_results = list_significant_values(model.summary(), threshold=threshold, print_results=False)
    print(f"Significant results: {len(significant_results)}/{len(X_columns)}")

    # Print QQ plot
    if print_qq:
        plot_qq(model, df[X_columns], df[y_column])

    #Create a list with the columns name significant results
    significant_columns = significant_results['feature'].tolist()
    #Add a column with the id of the column
    significant_results['col_id'] = significant_results['feature'].apply(lambda x: '_'.join(x.split('_')[1:]))

    # Map the columns name
    if map_columns_name != None:
        significant_results = map_columns_name(significant_results)

    # Add a column with the name of the column
    if colname and colname not in significant_results.columns:
        significant_results[colname] = significant_results['col_id']

    # Print results
    if print_results:
        # Print top and bottom results if too much significant results
        if len(significant_results) > limit_tops:
            print(f'\nTop {limit_tops//2}:')
            display(significant_results.head(limit_tops//2))
            print(f'\nBottom {limit_tops//2}:')
            display(significant_results.tail(limit_tops//2))
        # Otherwise print all results
        else:
            display(significant_results)
    
    # Plot barplot
    if plot_barplot:
        # Plot top and bottom results if too much significant results
        if len(significant_results) > limit_tops:
            plot_results(pd.concat([significant_results.head(limit_tops//2), significant_results.tail(limit_tops//2)]), colname, 'coef', title)
        # Otherwise plot all results    
        else:
            plot_results(significant_results, colname, 'coef', title)

    return significant_results, significant_columns    

def study_pearson(
    df,
    X_columns,
    y_column,
    colname='col_name',
    threshold=0.05,
    print_results=True,
    plot_barplot=True,
    title=None,
    map_columns_name=None,
    limit_tops=20
    ):
    """
    This function performs a Pearson correlation test on a dataset and returns the significant results.
    The function also plots the barplot of the significant results with the confidence interval.

    Parameters:
        df (DataFrame): The dataset to process
        X_columns (list): The list of features to use
        y_column (str): The target variable
        colname (str): The name of the column to use for the barplot
        threshold (float): The threshold to use for check if a feature is significant (t-test)
        print_results (bool): Whether to print the results or not
        plot_barplot (bool): Whether to plot the barplot or not
        title (str): The title of the barplot
        map_columns_name (function): A function to map the column names
        limit_tops (int): The number of top and bottom features to display

    Returns:
        significant_results (DataFrame): The significant results
        significant_columns (list): The list of significant columns
    """
    
    # Perform Pearson correlation test
    results = perform_pearsonr(df, X_columns, y_column, print_results=False)

    # Find and print results with p-values less than threshold
    results = results[results['p_value'] < threshold]
    print(f"Significant results: {len(results)}/{len(X_columns)}")

    significant_results = results.copy()

    # Create a list with the columns name significant results
    significant_columns = significant_results.index.tolist()

    # Add a column with the feature and a column with the id of the column
    significant_results['feature'] = significant_columns
    significant_results['col_id'] = significant_results.index.map(lambda x: '_'.join(x.split('_')[1:]))

    # Map the columns name
    if map_columns_name != None:
        significant_results = map_columns_name(significant_results)

    # Add a column with the name of the column
    if colname and colname not in significant_results.columns:
        significant_results[colname] = significant_results['col_id']

    # Print results
    if print_results:
        # Print top and bottom results if too much significant results
        if len(significant_results) > limit_tops:
            print(f'\nTop {limit_tops//2}:')
            display(significant_results.head(limit_tops//2))
            print(f'\nBottom {limit_tops//2}:')
            display(significant_results.tail(limit_tops//2))
        # Otherwise print all results
        else:
            display(significant_results)
    
    if plot_barplot:
        # Plot top and bottom results if too much significant results
        if len(significant_results) > limit_tops:
            plot_results(pd.concat([significant_results.head(limit_tops//2), significant_results.tail(limit_tops//2)]), colname, 'correlation', title)
        # Otherwise plot all results
        else:
            plot_results(significant_results, colname, 'correlation', title)

    return significant_results, significant_columns


def plot_qq(model, X, y):
    """
    Generate a QQ plot for the residuals of a regression model.
    The QQ plot allows to check if the residuals are normally distributed.

    Parameters:
        model (regression model): The fitted regression model.
        X (DataFrame): The input features.
        y (Series): The target variable.

    Returns:
        None
    """

    # Add constant to X
    X = sm.add_constant(X)

    # Predictions
    predictions = model.predict(X)

    # Residuals
    residuals = y - predictions

    # QQ plot
    fig, ax = plt.subplots(figsize=(6, 4))
    sm.qqplot(residuals, line='s', ax=ax)
    plt.title('QQ Plot of Residuals')
    plt.show()



def list_significant_values(model_summary, threshold=0.05, print_results=True):
    """
    Function to list the significant values of a regression model.

    Parameters:
        model_summary (regression model summary): The summary of the regression model.
        threshold (float): The threshold to use for check if a feature is significant (t-test)
        print_results (bool): Whether to print the results or not

    Returns:
        significant_values_df (DataFrame): The DataFrame containing the significant values
    """
    # Create a DataFrame with the significant feature from the model summary
    significant_values = []
    for row in model_summary.tables[1].data[2:]:
        # convert p-value to float
        if float(row[4]) < threshold:
            colname = row[0]
            significant_values.append([colname, float(row[1]), float(row[4]), float(row[5]), float(row[6])])

    # Convert the list of significant feature to a DataFrame sorted by coefficient
    significant_values_df = pd.DataFrame(significant_values, columns=['feature', 'coef', 'p_value', 'lower_ci', 'upper_ci'])
    significant_values_df = significant_values_df.sort_values(by='coef', ascending=False)

    # Print results
    if (print_results):
        # Print top and bottom results if too much significant results
        if (len(significant_values_df) > 20):
            display(significant_values_df.head(10))
            display(significant_values_df.tail(10))
        # Otherwise print all results
        else:
            display(significant_values_df)

    return significant_values_df

def perform_pearsonr(df, columns, target_column, print_results=False):
    """
    Function to perform a Pearson correlation test on a dataset. 
    The Pearson correlation test allows to check the correlation between two variables.

    Parameters:
        df (DataFrame): The dataset to process
        columns (list): The list of features to use
        target_column (str): The target variable
        print_results (bool): Whether to print the results or not

    Returns:
       results_df (DataFrame): The DataFrame containing the correlation results
    """
    # Create a dictionary to store the results
    correlation_results = {}

    # Perform Pearson correlation test for all columns
    for col in columns:
        # Perform Pearson correlation test
        res = pearsonr(df[col], df[target_column])
        ci = 0.95
        
        correlation = res[0]
        p_value = res[1]
        confidence_interval = res.confidence_interval(ci)

        # Store the results in a dictionary if there is a correlation
        if not np.isnan(correlation):
            correlation_results[col] = {'correlation': correlation, 'p_value': p_value, 'lower_ci': confidence_interval[0], 'upper_ci': confidence_interval[1]}

    results_df = pd.DataFrame.from_dict(correlation_results, orient='index').sort_values(by='correlation', ascending=False)

    # Print results
    if print_results:
        # Print top and bottom results if too much significant results
        if len(results_df) > 20:
            display(results_df.head(10))
            display(results_df.tail(10))
        # Otherwise print all results
        else:
            display(results_df)

    return results_df

# List movies of an actor
def list_movies_of_actor(df_actors, df_movies, actor_id, limit=None):
    """
    Function to list the movies of an actor.

    Parameters:
        df_actors (DataFrame): The actors dataset
        df_movies (DataFrame): The movies dataset
        actor_id (str): The id of the actor
        limit (int): The number of movies to return

    Returns:
        df_movies (DataFrame): The movies of the actor
    """
    # Get the movies ids of the actor
    movies_ids = df_actors[df_actors['freebase_actor_id'] == actor_id]['wikipedia_id'].unique()
    # Display the actor name
    display(df_actors[df_actors['freebase_actor_id'] == actor_id]['actor_name'].unique())

    #Remove movies id if there is a limit 
    if (limit != None):
        movies_ids = movies_ids[:limit]
        
    return df_movies[df_movies['wikipedia_id'].isin(movies_ids)]

def plot_results(df, y_column, x_column, title, figsize=(10, 5)):
    """
    Function to plot the results of a regression model.
    The plot can is a horizontal bar plot with the confidence interval.

    Parameters:
        df (DataFrame): The dataset where the results to plot are stored
        y_column (str): The column to use for the y-axis
        x_column (str): The column to use for the x-axis
        title (str): The title of the plot
        figsize (tuple): The size of the plot (width, height) - by default (10, 5)

    Returns:
        None
    """
    results = df.copy()

    # Check if there are results to plot
    if (len(results) == 0):
        print('No results to plot')
        return

    # Calculate the lower and upper confidence interval for the coefficient
    if 'upper_ci' in results.columns:
        results['ci_error'] = results['upper_ci'] - results[x_column]

    # Convert the y_column to string to avoid issues with seaborn
    results[y_column] = results[y_column].astype(str)

    # Create the plot
    plt.figure(figsize=figsize)

    # Create horizontal bar plot
    # If there is no ci_error column, we don't plot the confidence interval
    if 'ci_error' not in results.columns:
        sorted_results  = results.groupby(y_column)[x_column].mean().sort_values(ascending=False)
        bar = sns.barplot(x=x_column, y=y_column, data=results, order=sorted_results.index, hue=y_column, hue_order=sorted_results.index, palette='flare')
    # Otherwise we plot also the confidence interval
    else:
        bar = sns.barplot(x=x_column, y=y_column, data=results, order=results[y_column], hue=y_column, hue_order=results[y_column], palette='flare')

        # Get the y positions of the bars
        y_positions = bar.get_yticks()

        # Adjust positions based on the number of categories
        adjusted_positions = y_positions + bar.patches[0].get_height() / len(results[y_column]) / 2

        # Add error bars
        plt.errorbar(x=results[x_column], y=adjusted_positions, 
                     xerr=[results['ci_error'], results['ci_error']], 
                     fmt='none', color='black', capsize=0, elinewidth=3, markeredgewidth=0)
    
    # Set the title, labels and add a grid
    plt.ylabel(y_column)
    plt.xlabel(x_column)
    plt.title(title)
    plt.grid(True)

    #Remove the legend
    plt.legend([],[], frameon=False)

    #Resize the plot and show it
    plt.tight_layout()
    plt.show()

def filter_VIF(df, X_columns, threshold=5):
    """
    Function to filter the features based on the VIF score. 
    The VIF score is a measure of multicollinearity in a dataset. It is used to detect the correlation between features.

    Parameters:
        df (DataFrame): The dataset where the features are stored
        X_columns (list): The list of features to process
        threshold (float): The threshold to use for filtering

    Returns:
        X_columns (list): The filtered list of features
    """
    # Get the features
    X = df[X_columns]

    # Calculate VIF
    vif = pd.DataFrame()
    vif_factors = []
    for i in tqdm(range(X.shape[1])):
        vif_factors.append(variance_inflation_factor(X.values, i))

    vif["VIF Factor"] = vif_factors
    vif["features"] = X.columns

    # Filter features with a VIF score above the threshold
    vif_filtered = vif[vif['VIF Factor'] < threshold]

    return vif_filtered['features'].tolist()

def compare_baseline(model, df, X_columns, y_column, print_results=True):
    """
    Function to compare the baseline model (mean predictor) with the regression model.

    Parameters:
        model (regression model): The fitted regression model
        df (DataFrame): The dataset where the features are stored
        X_columns (list): The list of features to process
        y_column (str): The target variable
        print_results (bool): Whether to print the results or not

    Returns:
        None
    """
    # Get the features and target variable
    X = df[X_columns]
    y = df[y_column]

    # Add constant to X
    X = sm.add_constant(X)

    # Predictions
    y_pred = model.predict(X)

    # Evaluate metrics
    r2 = model.rsquared
    adjusted_r_squared = model.rsquared_adj
    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)

    # Baseline model (predicting mean)
    mean_y = np.mean(y)
    baseline_predictions = np.full(shape=y.shape, fill_value=mean_y)
    baseline_mse = mean_squared_error(y, baseline_predictions)
    baseline_mae = mean_absolute_error(y, baseline_predictions)
    baseline_r2 = r2_score(y, baseline_predictions)
    baseline_adjusted_r2 = baseline_r2

    # Compute percentage of improvement
    improvement_mse =  (str(np.round((mse - baseline_mse) / baseline_mse * 100, 2)) + '%' if baseline_mse != 0 else 'inf')
    improvement_mae = (str(np.round((mae - baseline_mae) / baseline_mae * 100, 2)) + '%' if baseline_mae != 0 else 'inf')
    improvement_r2 = (str(np.round((r2 - baseline_r2) / baseline_r2 * 100, 2)) + '%' if baseline_r2 != 0 else 'inf')
    improvement_adjusted_r2 = improvement_r2

    results_df = pd.DataFrame({'r2': [r2, baseline_r2, improvement_r2], 'r2-adj': [adjusted_r_squared, baseline_adjusted_r2, improvement_adjusted_r2], 'mae': [mae, baseline_mae, improvement_mae], 'mse': [mse, baseline_mse, improvement_mse]}, index=['model', 'baseline', 'improvement'])

    # Print results
    if print_results:
        
        print('\n\n-- Baseline Comparaison --')
        display(results_df)
    else:
        return results_df

def export_json(df, filename):
    """
    Function to export a DataFrame to a JSON file. 
    This function is used to export data for the visualization on website. 

    Parameters:
        df (DataFrame): The dataset to export
        filename (str): The name of the JSON file

    Returns:
        None
    """
    
    # Add the standard error column
    if 'coef' in df.columns and 'sem' not in df.columns and 'upper_ci' in df.columns:
        df['sem'] = df['upper_ci'] - df['coef'] 
    elif 'correlation' in df.columns and 'sem' not in df.columns and 'upper_ci' in df.columns:
        df['sem'] = df['upper_ci'] - df['correlation']
    
    # Export the dataset to JSON
    df.to_json(filename, orient='records')

def plot_specific_scatter(df, column, value):
    """
    Function to plot a scatterplot and rating_difference distribution for a specific feature value.

    Parameters:
        df (DataFrame): The dataset to use
        column (str): The column to use as specific feature (like genre, country, etc.)
        value (str): The value to use for filtering the specific feature

    Returns:
        None
    """
    
    # Filter the dataset
    df_value = df[df[column] == value]
    fig, ax = plt.subplots(1, 2, figsize=(12,5))

    # plot the scatterplot
    sns.scatterplot(x="metascore", y="imdb_rating_scaled", data=df_value, ax=ax[0], color='#67001f')
    ax[0].set_title(f"IMDb Users Rating vs Metascore for {column} = {value}")
    ax[0].set_xticks(range(0, 101, 10))
    ax[0].set_yticks(range(0, 101, 10))
    ax[0].set_xlim(0, 100)
    ax[0].set_ylim(0, 100)
    ax[0].set_xlabel("Metascore")
    ax[0].set_ylabel("IMDb Users Rating")
    ax[0].grid()

    # plot a line of the mean imdb rating and metascore for the specific feature
    ax[0].axhline(y=df_value['imdb_rating_scaled'].mean(), color='r', linestyle='-')
    ax[0].axvline(x=df_value['metascore'].mean(), color='r', linestyle='-')

    # plot a line of the mean imdb rating and metascore for the whole dataset
    ax[0].axhline(y=df['imdb_rating_scaled'].mean(), color='black', linestyle='-')
    ax[0].axvline(x=df['metascore'].mean(), color='black', linestyle='-')

    # plot the diagonal x=y
    ax[0].plot([0, 100], [0, 100], color='black', linestyle='-', linewidth=1, alpha=0.5)

    # plot the rating difference distribution
    sns.histplot(df_value['rating_difference'], stat='count', alpha=0.5, ax=ax[1], color='#67001f', bins=20)
    # plot a line of the mean rating difference for the specific feature
    ax[1].axvline(df_value['rating_difference'].mean(), color='r')
    # plot a line of the mean rating difference for the whole dataset
    ax[1].axvline(df['rating_difference'].mean(), color='black')
    #Set the label and title
    ax[1].set_xlabel('Rating Difference')
    ax[1].set_ylabel('Count')
    ax[1].set_title(f"Rating difference distribution for {column} = {value}")
    
    #add a legend
    blue_line = mlines.Line2D([], [], color='red', label='Specific Mean')
    red_line = mlines.Line2D([], [], color='black', label='Overall Mean')
    ax[1].legend(handles=[blue_line, red_line])

    #resize the plot and show it
    fig.tight_layout()
    plt.show()