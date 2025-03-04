import pandas as pd
import json
import logging

logger = logging.getLogger(__name__)

def convert_to_dataset_format(movie_data, rating_data):
    """
    Convertit les données au format attendu par l'API Azure ML.
    
    Args:
        movie_data (dict): Données du film (Movie ID, Movie Name)
        rating_data (dict): Données de notation (UserId, MovieId, Rating, Timestamp)
        
    Returns:
        dict: Données formatées pour l'API Azure ML
    """
    try:
        # Création des DataFrames à partir des dictionnaires
        movie_df = pd.DataFrame([movie_data])
        rating_df = pd.DataFrame([rating_data])
        
        # Renommage des colonnes pour correspondre au format attendu
        movie_df = movie_df.rename(columns={
            'movie_id': 'Movie ID',
            'movie_name': 'Movie Name'
        })
        
        rating_df = rating_df.rename(columns={
            'user_id': 'UserId',
            'movie_id': 'MovieId',
            'rating': 'Rating',
            'timestamp': 'Timestamp'
        })
        
        # Conversion des types de données
        movie_df['Movie ID'] = movie_df['Movie ID'].astype(int)
        rating_df['UserId'] = rating_df['UserId'].astype(int)
        rating_df['MovieId'] = rating_df['MovieId'].astype(int)
        rating_df['Rating'] = rating_df['Rating'].astype(int)  
        rating_df['Timestamp'] = rating_df['Timestamp'].astype(int)
        
        # Format standard - Basé sur la structure de l'API
        # Inversé comme demandé: WebServiceInput0 pour les ratings, WebServiceInput1 pour les films
        formatted_data = {
            "Inputs": {
                "WebServiceInput0": rating_df.to_dict(orient='records'),
                "WebServiceInput1": movie_df.to_dict(orient='records')
            }
        }
        
        logger.info(f"Données converties (format standard): {formatted_data}")
        return formatted_data
    
    except Exception as e:
        logger.error(f"Erreur lors de la conversion des données: {str(e)}")
        raise

def try_different_formats(movie_data, rating_data):
    """
    Essaie différents formats de données pour l'API Azure ML.
    
    Args:
        movie_data (dict): Données du film
        rating_data (dict): Données de notation
        
    Returns:
        list: Liste des différents formats à essayer
    """
    formats = []
    
    # Format 1: Format standard avec inputs inversés
    formats.append(convert_to_dataset_format(movie_data, rating_data))
    
    # Format 2: Correction des noms de colonnes pour la jointure
    # Basé sur la jointure observée dans l'interface Azure ML
    formats.append({
        "Inputs": {
            "WebServiceInput0": [{
                "UserId": rating_data['user_id'],
                "MovieId": rating_data['movie_id'],
                "Rating": int(rating_data['rating']),
                "Timestamp": rating_data['timestamp']
            }],
            "WebServiceInput1": [{
                "Movie ID": movie_data['movie_id']
            }]
        }
    })
    
    # Format 3: Utilisation de noms de colonnes exacts comme dans la jointure
    formats.append({
        "Inputs": {
            "WebServiceInput0": [{
                "UserId": rating_data['user_id'],
                "MovieId": rating_data['movie_id'],
                "Rating": int(rating_data['rating']),
                "Timestamp": rating_data['timestamp']
            }],
            "WebServiceInput1": [{
                "Movie ID": movie_data['movie_id'],
                "Movie Name": movie_data['movie_name']
            }]
        }
    })
    
    # Format 4: Utilisation d'un seul input avec toutes les données
    formats.append({
        "Inputs": {
            "input1": [{
                "Movie ID": movie_data['movie_id'],
                "Movie Name": movie_data['movie_name'],
                "UserId": rating_data['user_id'],
                "MovieId": rating_data['movie_id'],
                "Rating": int(rating_data['rating']),
                "Timestamp": rating_data['timestamp']
            }]
        }
    })
    
    # Format 5: Utilisation de noms d'entrée génériques
    formats.append({
        "Inputs": {
            "input1": [{
                "UserId": rating_data['user_id'],
                "MovieId": rating_data['movie_id'],
                "Rating": int(rating_data['rating']),
                "Timestamp": rating_data['timestamp']
            }],
            "input2": [{
                "Movie ID": movie_data['movie_id'],
                "Movie Name": movie_data['movie_name']
            }]
        }
    })
    
    # Format 6: Utilisation de données au format CSV
    movie_csv = f"Movie ID,Movie Name\n{movie_data['movie_id']},{movie_data['movie_name']}"
    rating_csv = f"UserId,MovieId,Rating,Timestamp\n{rating_data['user_id']},{rating_data['movie_id']},{int(rating_data['rating'])},{rating_data['timestamp']}"
    
    formats.append({
        "Inputs": {
            "WebServiceInput0": rating_csv,
            "WebServiceInput1": movie_csv
        }
    })
    
    return formats
