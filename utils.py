from ast import literal_eval
import pandas as pd
from scipy.stats import pearsonr
import statsmodels.api as sm
import numpy as np
import json
from sklearn.model_selection import KFold
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from tqdm import tqdm
import matplotlib.pyplot as plt
import itertools
import networkx as nx
import matplotlib.lines as mlines

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

def perform_OLS(df, X_columns, y_column, print_results=True):
    X = df[X_columns]
    y = df[y_column]

    X = sm.add_constant(X)

    # Fit the OLS model
    model = sm.OLS(y, X).fit()

    if print_results:
        display(model.summary().tables[0])

    return model


def list_significant_values(model_summary, threshold=0.05, print_results=True):
    significant_values = []
    for row in model_summary.tables[1].data[2:]:
        # convert p-value to float
        if float(row[4]) < threshold:
            colname = row[0]
            significant_values.append([colname, float(row[1]), float(row[4]), float(row[5]), float(row[6])])

    # Convert the list of significant genres to a DataFrame
    significant_values_df = pd.DataFrame(significant_values, columns=['colname', 'coef', 'p_value', 'lower_ci', 'upper_ci'])
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


def perform_SVR(df, X_columns, y_column, kfolds=5, metrics=['r2', 'mae', 'mse'], print_results=True):


    X = df[X_columns]
    y = df[y_column]

    kf = KFold(n_splits=kfolds, shuffle=True, random_state=42)

    results = []
    for train_index, test_index in tqdm(kf.split(X)):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        svr = SVR(kernel='rbf', C=1e3, gamma=0.1)
        svr.fit(X_train, y_train)

        y_pred = svr.predict(X_test)

        result = {}

        # Evaluate metrics
        if 'r2' in metrics:
            r2 = svr.score(X_test, y_test)
            result['r2'] = r2

        if 'mae' in metrics:
            mae = mean_absolute_error(y_test, y_pred)
            result['mae'] = mae

        if 'mse' in metrics:
            mse = mean_squared_error(y_test, y_pred)
            result['mse'] = mse

        results.append(result)

    results_df = pd.DataFrame(results)

    # Add the mean and std of the metrics as first and second row
    results_df.loc['mean'] = results_df.mean()
    results_df.loc['std'] = results_df.std()

    if print_results:
        display(results_df)

    return results_df


def plot_results(df, y_column, x_column, title, figsize=(10, 5)):
    results = df.copy()

    # Calculate the lower and upper confidence interval for the coefficient
    if 'upper_ci' in results.columns:
        results['ci_error'] = results['upper_ci'] - results[x_column]

    results[y_column] = results[y_column].astype(str)

    # Create the plot
    plt.figure(figsize=figsize)

    # Create horizontal bar plot
    if 'ci_error' not in results.columns:
        plt.barh(results[y_column], results[x_column], color='skyblue')
    else:
        plt.barh(results[y_column], results[x_column], xerr=[results['ci_error'], results['ci_error']], color='skyblue')

    plt.ylabel(y_column)
    plt.xlabel(x_column)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

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

    print('\n\n--------------------------------------\n')
    print(f"Significant results: {len(interactions_ols_significant_results)}/{len(interactions_columns)}")


    # Add the column names
    interactions_ols_significant_results['col1'] = interactions_ols_significant_results['colname'].apply(lambda x: x.split('_x_')[0])
    interactions_ols_significant_results['col2'] = interactions_ols_significant_results['colname'].apply(lambda x: x.split('_x_')[1])

    print('\nTop 15:')
    display(interactions_ols_significant_results.head(15))
    
    print('\nBottom 15:')
    display(interactions_ols_significant_results.tail(15))

    # Plot the first 15 and last 15 tropes in the same plot
    plot_results(pd.concat([interactions_ols_significant_results.head(15), interactions_ols_significant_results.tail(15)]), 'colname', 'coef', "OLS Coefficients for Significant Features", figsize=(20, 10))

    # Count the number of movies per value
    values_count = one_hot[one_hot_columns].sum().to_dict()

    # Plot the graph network
    plot_graph(interactions_ols_significant_results, values_count, title)

    return interactions_ols_significant_results

