from ast import literal_eval
import pandas as pd
from scipy.stats import pearsonr
import statsmodels.api as sm
import numpy as np
import json


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
    # Create a new dataframe with the one hot encoded columns
    one_hot_df = pd.get_dummies(df, columns=[column], prefix=prefix)

    # Removing symbols from column names to make the regression model work
    #for ch in ['/', ' ', "'", '-', '&', '[', ']']:
        #one_hot_df.columns = one_hot_df.columns.str.replace(ch, "")
    
    one_hot_columns = list(filter(lambda x: x.startswith(prefix), one_hot_df.columns))

    # Convert bool to int
    one_hot_df[one_hot_columns] = one_hot_df[one_hot_columns].astype(int)

    one_hot_df = one_hot_df.groupby(id_column)[one_hot_columns].sum().reset_index()
    
    return one_hot_df[[id_column] + one_hot_columns], one_hot_columns

def perform_OLS(df, X_columns, y_column):
    X = df[X_columns]
    y = df[y_column]

    X = sm.add_constant(X)

    # Fit the OLS model
    model = sm.OLS(y, X).fit()

    # Print out the statistics
    model_summary = model.summary()
    return model_summary

def list_significant_values(model_summary, threshold=0.05, print_results=True):
    significant_values = []
    for row in model_summary.tables[1].data[2:]:
        # convert p-value to float
        if float(row[4]) < threshold:
            colname = row[0]
            significant_values.append([colname, float(row[1]), float(row[4])])

    # Convert the list of significant genres to a DataFrame
    significant_values_df = pd.DataFrame(significant_values, columns=['colname', 'coef', 'p_value'])
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
        correlation, p_value = pearsonr(df[col], df[target_column])
        if not np.isnan(correlation):
            correlation_results[col] = {'correlation': correlation, 'p_value': p_value}

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