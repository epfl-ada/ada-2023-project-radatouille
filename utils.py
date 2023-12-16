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

def process_tropes(df, characters_data):
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

    df_tropes = df.copy()

    df_tropes[['character_name', 'movie_name', 'freebase_actor_map_id', 'actor_name']] = df_tropes['character'].apply(lambda x: extract_character(x)).apply(pd.Series)

    # Add freebase_id of movie from characters_data based on freebase_actor_map_id
    df_tropes = pd.merge(df_tropes, characters_data[['freebase_actor_map_id', 'freebase_id']], on='freebase_actor_map_id', how='left')

    # Drop nan values
    df_tropes.dropna(subset=['freebase_id'], inplace=True)
    df_tropes = df_tropes.reset_index(drop=True)

    return df_tropes


def hotencode(df, column, id_column, prefix='onehot'):

    df_filtered = df[[id_column, column]]

    # Create a new dataframe with the one hot encoded columns
    one_hot_df = pd.get_dummies(df_filtered, columns=[column], prefix=prefix)

    # Removing symbols from column names to make the regression model work
    #for ch in ['/', ' ', "'", '-', '&', '[', ']']:
        #one_hot_df.columns = one_hot_df.columns.str.replace(ch, "")
    
    one_hot_columns = list(filter(lambda x: x.startswith(prefix), one_hot_df.columns))

    # Group by id_column and aggregate using max to ensure values are 0 or 1
    one_hot_df = one_hot_df.groupby(id_column)[one_hot_columns].max().astype('int').reset_index()
    
    return one_hot_df, one_hot_columns

def perform_OLS(df, X_columns, y_column, regularization=None, alpha=1.0, print_results=True):
    x = df[X_columns]
    y = df[y_column]

    X = sm.add_constant(x)
    model = sm.OLS(y, X)

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
    model = perform_OLS(df, X_columns, y_column, regularization=regularization, alpha=alpha)
    summary = model.summary()

    if print_baseline:
        compare_baseline(model, df, X_columns, y_column, print_results=True)


    # Find results with p-values less than threshold
    significant_results = list_significant_values(model.summary(), threshold=threshold, print_results=False)

    print(f"Significant results: {len(significant_results)}/{len(X_columns)}")

    if print_qq:
        plot_qq(model, df[X_columns], df[y_column])

    significant_columns = significant_results['feature'].tolist()
    significant_results['col_id'] = significant_results['feature'].apply(lambda x: '_'.join(x.split('_')[1:]))

    if map_columns_name != None:
        significant_results = map_columns_name(significant_results)

    if colname and colname not in significant_results.columns:
        significant_results[colname] = significant_results['col_id']

    if print_results:
        if len(significant_results) > limit_tops:
            print(f'\nTop {limit_tops//2}:')
            display(significant_results.head(limit_tops//2))
            print(f'\nBottom {limit_tops//2}:')
            display(significant_results.tail(limit_tops//2))
        else:
            display(significant_results)
    
    if plot_barplot:
        if len(significant_results) > limit_tops:
            plot_results(pd.concat([significant_results.head(limit_tops//2), significant_results.tail(limit_tops//2)]), colname, 'coef', title)
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
    results = perform_pearsonr(df, X_columns, y_column, print_results=False)

    # Find results with p-values less than threshold
    results = results[results['p_value'] < threshold]

    print(f"Significant results: {len(results)}/{len(X_columns)}")

    significant_results = results.copy()
    significant_columns = significant_results.index.tolist()
    significant_results['feature'] = significant_columns
    significant_results['col_id'] = significant_results.index.map(lambda x: '_'.join(x.split('_')[1:]))

    if map_columns_name != None:
        significant_results = map_columns_name(significant_results)

    if colname and colname not in significant_results.columns:
        significant_results[colname] = significant_results['col_id']

    if print_results:
        if len(significant_results) > limit_tops:
            print(f'\nTop {limit_tops//2}:')
            display(significant_results.head(limit_tops//2))
            print(f'\nBottom {limit_tops//2}:')
            display(significant_results.tail(limit_tops//2))
        else:
            display(significant_results)
    
    if plot_barplot:
        if len(significant_results) > limit_tops:
            plot_results(pd.concat([significant_results.head(limit_tops//2), significant_results.tail(limit_tops//2)]), colname, 'correlation', title)
        else:
            plot_results(significant_results, colname, 'correlation', title)

    return significant_results, significant_columns


def plot_qq(model, X, y):
    """
    Generate a QQ plot for the residuals of a regression model.

    Parameters:
    model (regression model): The fitted regression model.
    X (DataFrame): The input features.
    y (Series): The target variable.
    """

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
    significant_values = []
    for row in model_summary.tables[1].data[2:]:
        # convert p-value to float
        if float(row[4]) < threshold:
            colname = row[0]
            significant_values.append([colname, float(row[1]), float(row[4]), float(row[5]), float(row[6])])

    # Convert the list of significant genres to a DataFrame
    significant_values_df = pd.DataFrame(significant_values, columns=['feature', 'coef', 'p_value', 'lower_ci', 'upper_ci'])
    significant_values_df = significant_values_df.sort_values(by='coef', ascending=False)

    if (print_results):
        if (len(significant_values_df) > 20):
            display(significant_values_df.head(10))
            display(significant_values_df.tail(10))
        else:
            display(significant_values_df)

    return significant_values_df

def perform_pearsonr(df, columns, target_column, print_results=False):
    correlation_results = {}
    for col in columns:
        res = pearsonr(df[col], df[target_column])
        ci = 0.95
        
        correlation = res[0]
        p_value = res[1]
        confidence_interval = res.confidence_interval(ci)

        if not np.isnan(correlation):
            correlation_results[col] = {'correlation': correlation, 'p_value': p_value, 'lower_ci': confidence_interval[0], 'upper_ci': confidence_interval[1]}

    results_df = pd.DataFrame.from_dict(correlation_results, orient='index').sort_values(by='correlation', ascending=False)

    if print_results:
        if len(results_df) > 20:
            display(results_df.head(10))
            display(results_df.tail(10))
        else:
            display(results_df)

    return results_df

# List movies of an actor
def list_movies_of_actor(df_actors, df_movies, actor_id, limit=None):
    movies_ids = df_actors[df_actors['freebase_actor_id'] == actor_id]['wikipedia_id'].unique()
    display(df_actors[df_actors['freebase_actor_id'] == actor_id]['actor_name'].unique())

    if (limit != None):
        movies_ids = movies_ids[:limit]
        
    return df_movies[df_movies['wikipedia_id'].isin(movies_ids)]

def plot_results(df, y_column, x_column, title, figsize=(10, 5)):
    results = df.copy()

    if (len(results) == 0):
        print('No results to plot')
        return

    # Calculate the lower and upper confidence interval for the coefficient
    if 'upper_ci' in results.columns:
        results['ci_error'] = results['upper_ci'] - results[x_column]

    results[y_column] = results[y_column].astype(str)

    # Create the plot
    plt.figure(figsize=figsize)

    # Create horizontal bar plot
    if 'ci_error' not in results.columns:
        sorted_results  = results.groupby(y_column)[x_column].mean().sort_values(ascending=False)
        bar = sns.barplot(x=x_column, y=y_column, data=results, order=sorted_results.index, hue=y_column, hue_order=sorted_results.index, palette='flare', legend=False)
    else:
        bar = sns.barplot(x=x_column, y=y_column, data=results, order=results[y_column], hue=y_column, hue_order=results[y_column], palette='flare', legend=False)

        y_positions = bar.get_yticks()
        # Adjust positions based on the number of categories
        adjusted_positions = y_positions + bar.patches[0].get_height() / len(results[y_column]) / 2

        # Add error bars
        plt.errorbar(x=results[x_column], y=adjusted_positions, 
                     xerr=[results['ci_error'], results['ci_error']], 
                     fmt='none', color='black', capsize=0, elinewidth=3, markeredgewidth=0)

    
    plt.ylabel(y_column)
    plt.xlabel(x_column)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def filter_VIF(df, X_columns, threshold=5):
    """
    Function to filter the features based on the VIF score
    Parameters:
        df (DataFrame): The dataset to process
        X_columns (list): The list of features to process
        threshold (float): The threshold to use for filtering
    Returns:
        X_columns (list): The filtered list of features
    """

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

def compute_interactions(df, columns):
    interaction_df = df.copy()

    pairs = itertools.combinations(df[columns].columns, 2)

    for col1, col2 in pairs:
        interaction_term = col1 + "_x_" + col2
        interaction_df = pd.concat([interaction_df, pd.Series(df[col1] * df[col2], name=interaction_term)], axis=1)

    return interaction_df



def plot_graph(pairs_results, values_counts, title):

    G = nx.Graph()


    unique_values = set(pairs_results['col1']).union(set(pairs_results['col2']))

    # Add nodes with sizes based on value counts
    for value in unique_values:
        node_size = values_counts.get(value, 0)
        G.add_node(value, size=node_size)

    # Add weighted edges based on coefficients
    for _, row in pairs_results.iterrows():
        col1, col2, weight = row['col1'], row['col2'], row['coef']
        color = 'skyblue' if weight > 0 else 'tomato'
        G.add_edge(col1, col2, weight=abs(weight), color=color)

    # Extract edge weights and scale for visualization
    edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
    # Extract node sizes and scale for visualization
    node_sizes = [G.nodes[node]['size'] * 10 for node in G.nodes()]  # Scale as needed

    # Extract edge colors
    edge_colors = [G[u][v]['color'] for u, v in G.edges()]

    # Draw the graph with a spring layout
    plt.figure(figsize=(15, 15))

    # Higher k values cause more spread.
    pos = nx.spring_layout(G, k=10, iterations=100)  # Adjust k as needed

    custom_labels = {node: '_'.join(node.split('_')[:1]) if len(node.split('_')) > 2 else node.split('_')[1] if len(node.split('_')) == 2 else node for node in G.nodes()}

    nx.draw(G, pos, with_labels=True, node_size=node_sizes, width=edge_weights, edge_color=edge_colors, labels=custom_labels, node_color='lightgrey')

    # Create custom lines for the legend
    blue_line = mlines.Line2D([], [], color='skyblue', marker='_', markersize=15, label='Positive Coefficient (Critics > Audience)')
    red_line = mlines.Line2D([], [], color='tomato', marker='_', markersize=15, label='Negative Coefficient (Critics < Audience)')

    # Add the legend to the plot
    plt.legend(handles=[blue_line, red_line])

    plt.title(title)
    plt.show()

def compute_interactions(df, columns):
    interaction_df = pd.DataFrame()

    pairs = itertools.combinations(df[columns].columns, 2)

    for col1, col2 in pairs:
        interaction_term = col1 + "_x_" + col2
        interaction_df = pd.concat([interaction_df, pd.Series(df[col1] * df[col2], name=interaction_term)], axis=1)

    return interaction_df

def full_study(df, column, id_column, threshold=0.005, title="OLS Coefficients for Significant Features"):
    # Hot encode the column
    one_hot, one_hot_columns = hotencode(df, column, id_column=id_column, prefix='onehot')
    
    # Add the rating_difference column
    one_hot = one_hot.merge(df[['freebase_id', 'rating_difference']].drop_duplicates(), on='freebase_id')

    # Set the index to freebase_id
    one_hot = one_hot.set_index('freebase_id')

    # Perform pearsonr
    one_hot_pearsonr_results = perform_pearsonr(one_hot, one_hot_columns, 'rating_difference', print_results=True)

    # Get the significant results
    significant_columns = one_hot_pearsonr_results[one_hot_pearsonr_results['p_value'] < threshold].index.tolist()

    print('\n\n--------------------------------------\n')
    print(f"Significant results: {len(significant_columns)}/{len(one_hot_columns)}")

    # Study the interactions
    study_interactions(one_hot, significant_columns, threshold=threshold, title=title)


def study_interactions(one_hot, significant_columns, threshold=0.005, title="OLS Coefficients for Significant Features"):

    one_hot_columns = one_hot.drop(columns=['rating_difference']).columns
    
    # Compute interaction dataframe between the significant columns
    interactions = compute_interactions(one_hot, significant_columns)
    interactions_columns = interactions.columns

    # Merge the interactions with the rating_difference column
    interactions = interactions.merge(one_hot[['rating_difference']], right_index=True, left_index=True)

    # Perform OLS on the interactions
    interactions_ols_model = perform_OLS(interactions, interactions_columns, 'rating_difference')
    interactions_ols_summary = interactions_ols_model.summary()

    # Get the significant results
    interactions_ols_significant_results = list_significant_values(interactions_ols_model.summary(), threshold=threshold, print_results=False)

    interactions_ols_significant_results.sort_values(by='coef', ascending=False, inplace=True)

    print('\n\n--------------------------------------\n')
    print(f"Significant results: {len(interactions_ols_significant_results)}/{len(interactions_columns)}")


    # Add the column names
    interactions_ols_significant_results['col1'] = interactions_ols_significant_results['feature'].apply(lambda x: x.split('_x_')[0])
    interactions_ols_significant_results['col2'] = interactions_ols_significant_results['feature'].apply(lambda x: x.split('_x_')[1])

    if len(interactions_ols_significant_results) > 30:
        print('\nTop 15:')
        display(interactions_ols_significant_results.head(15))

        print('\nBottom 15:')
        display(interactions_ols_significant_results.tail(15))

         # Plot the first 15 and last 15 tropes in the same plot
        plot_results(pd.concat([interactions_ols_significant_results.head(15), interactions_ols_significant_results.tail(15)]), 'feature', 'coef', "OLS Coefficients for Significant Features", figsize=(20, 10))

    else:
        display(interactions_ols_significant_results)

        plot_results(interactions_ols_significant_results, 'feature', 'coef', "OLS Coefficients for Significant Features", figsize=(20, 10))

   

    # Count the number of movies per value
    values_count = one_hot[one_hot_columns].sum().to_dict()

    # Plot the graph network
    plot_graph(interactions_ols_significant_results, values_count, title)

    return interactions_ols_significant_results


def compare_baseline(model, df, X_columns, y_column, print_results=True):
    X = df[X_columns]
    y = df[y_column]

    X = sm.add_constant(X)

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

    if print_results:
        
        print('\n\n-- Baseline Comparaison --')
        display(results_df)
    else:
        return results_df
    

def compare_plot_results(df1, df2, y_column, x_column1, x_column2, title1, title2, figsize=(10, 5)):
    results1 = df1.copy()
    results2 = df2.copy()

    # Calculate the lower and upper confidence interval for the coefficient
    if 'upper_ci' in results1.columns:
        results1['ci_error'] = results1['upper_ci'] - results1[x_column1]

    if 'upper_ci' in results2.columns:
        results2['ci_error'] = results2['upper_ci'] - results2[x_column2]

    results1[y_column] = results1[y_column].astype(str)
    results2[y_column] = results2[y_column].astype(str)

    # Create the plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)

    # Create horizontal bar plot
    bar1 = sns.barplot(x=x_column1, y=y_column, data=results1, order=results1[y_column], ax=ax1)
    bar2 = sns.barplot(x=x_column2, y=y_column, data=results2, order=results2[y_column], ax=ax2)

    if 'ci_error' in results1.columns:
        y_positions1 = bar1.get_yticks()
        # Adjust positions based on the number of categories
        adjusted_positions1 = y_positions1 + bar1.patches[0].get_height() / len(results1[y_column]) / 2

        # Add error bars
        ax1.errorbar(x=results1[x_column1], y=adjusted_positions1, 
                     xerr=[results1['ci_error'], results1['ci_error']], 
                     fmt='none', color='black', capsize=0, elinewidth=3, markeredgewidth=0)
        
    if 'ci_error' in results2.columns:
        y_positions2 = bar2.get_yticks()
        # Adjust positions based on the number of categories
        adjusted_positions2 = y_positions2 + bar2.patches[0].get_height() / len(results2[y_column]) / 2

        # Add error bars
        ax2.errorbar(x=results2[x_column2], y=adjusted_positions2, 
                     xerr=[results2['ci_error'], results2['ci_error']], 
                     fmt='none', color='black', capsize=0, elinewidth=3, markeredgewidth=0)
    ax1.set_ylabel(y_column)
    ax1.set_xlabel(x_column1)
    ax1.set_title(title1)
    ax1.grid(True)

    ax2.set_ylabel(y_column)
    ax2.set_xlabel(x_column2)
    ax2.set_title(title2)
    ax2.grid(True)

    plt.tight_layout()
    plt.show()


def venn_plot(vif_list, pearson_list, ols_list):
    plt.figure(figsize=(5,5))
    venn3([
        set(pearson_list),
        set(vif_list),
        set(ols_list)
        ], set_labels = ('Pearson', 'VIF', 'OLS'))
        
    plt.show()
def compare_ols_pearson(ols_results, pearsonr_results, ols_significant, pearsonr_significant, vif_significant, global_columns, colname, venn=True):
    print(f"Genres after Pearson filtering: {len(pearsonr_significant)}/{len(global_columns)}")
    print(f"Genres after VIF filtering: {len(vif_significant)}/{len(pearsonr_significant)}")
    print(f"Genres after OLS filtering: {len(ols_significant)}/{len(vif_significant)}")

    if venn:
        venn_plot(vif_significant, pearsonr_significant, ols_significant)

    # Display results that are in ols but NOT in pearson
    ols_not_pearson_significant = list(set(ols_significant).difference(set(pearsonr_significant)))
    print("Features that are in OLS but not in Pearson:")
    display(ols_results.loc[ols_results['feature'].isin(ols_not_pearson_significant)])

    # Display results that are in pearson AND ols
    ols_pearson_significant = list(set(pearsonr_significant).intersection(set(ols_significant)))
    ols_pearson_coef = ols_results.merge(pearsonr_results[['col_id', 'correlation']], on='col_id')
    print("Features that are in OLS and Pearson:")
    display(ols_pearson_coef)
    plot_results(ols_pearson_coef, colname, 'coef', title='OLS Coefficient for OLS and Pearson significant')

def export_json(df, filename):
    if 'coef' in df.columns and 'sem' not in df.columns and 'upper_ci' in df.columns:
        df['sem'] = df['upper_ci'] - df['coef'] 
    elif 'correlation' in df.columns and 'sem' not in df.columns and 'upper_ci' in df.columns:
        df['sem'] = df['upper_ci'] - df['correlation']
    df.to_json(filename, orient='records')


def plot_specific_scatter(df, column, value):
    df_value = df[df[column] == value]
    fig, ax = plt.subplots(1, 2, figsize=(10,5))

    sns.scatterplot(x="metascore", y="imdb_rating_scaled", data=df_value, ax=ax[0], color='#67001f')
    ax[0].set_title(f"IMDb Users Rating vs Metascore for {value}")
    ax[0].set_xticks(range(0, 101, 10))
    ax[0].set_yticks(range(0, 101, 10))
    ax[0].set_xlim(0, 100)
    ax[0].set_ylim(0, 100)
    ax[0].set_xlabel("Metascore")
    ax[0].set_ylabel("IMDb Users Rating")
    ax[0].grid()

    ax[0].axhline(y=df_value['imdb_rating_scaled'].mean(), color='r', linestyle='-')
    ax[0].axvline(x=df_value['metascore'].mean(), color='r', linestyle='-')

    ax[0].axhline(y=df['imdb_rating_scaled'].mean(), color='black', linestyle='-')
    ax[0].axvline(x=df['metascore'].mean(), color='black', linestyle='-')

    # plot the diagonal x=y
    ax[0].plot([0, 100], [0, 100], color='black', linestyle='-', linewidth=1, alpha=0.5)

    # set the hue to the bin order"
    sns.histplot(df_value['rating_difference'], stat='count', alpha=0.5, ax=ax[1], color='#67001f', bins=20)
    ax[1].axvline(df_value['rating_difference'].mean(), color='r')
    ax[1].axvline(df['rating_difference'].mean(), color='black')
    ax[1].set_xlabel('Rating Difference')
    ax[1].set_ylabel('Count')
    


    blue_line = mlines.Line2D([], [], color='red', label='Specific Mean')
    red_line = mlines.Line2D([], [], color='black', label='Overall Mean')
    ax[1].legend(handles=[blue_line, red_line])

    fig.tight_layout()

    plt.show()