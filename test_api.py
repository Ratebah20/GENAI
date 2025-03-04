import requests
import json
import logging
import sys
import os
from dotenv import load_dotenv
from data_converter import try_different_formats

# Configuration du logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Chargement des variables d'environnement
load_dotenv()

# Configuration de l'API Azure ML
AZURE_ML_ENDPOINT = "http://868c7bfc-60e0-4ecb-aa6a-ae0403081c17.francecentral.azurecontainer.io/score"
API_KEY = "4fqkvToeHnkRLgVi2pStArbyUPbcKKqH" # Remplacer par votre clé API réelle

def test_api_format(format_index, movie_data, rating_data):
    """
    Teste un format spécifique d'envoi de données à l'API Azure ML.
    
    Args:
        format_index (int): Index du format à tester (1-6)
        movie_data (dict): Données du film
        rating_data (dict): Données de notation
        
    Returns:
        tuple: (success, response_text)
    """
    # Obtenir tous les formats disponibles
    all_formats = try_different_formats(movie_data, rating_data)
    
    # Vérifier que l'index est valide
    if format_index < 1 or format_index > len(all_formats):
        logger.error(f"Format index {format_index} invalide. Doit être entre 1 et {len(all_formats)}")
        return False, f"Format index {format_index} invalide"
    
    # Sélectionner le format à tester
    input_data = all_formats[format_index - 1]
    
    # Afficher le format utilisé
    logger.info(f"Test du format {format_index}:")
    logger.info(json.dumps(input_data, indent=2))
    
    # Configuration des en-têtes
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    try:
        # Appel à l'API Azure ML
        response = requests.post(AZURE_ML_ENDPOINT, 
                               json=input_data, 
                               headers=headers)
        
        # Afficher le code de statut et la réponse
        logger.info(f"Code de statut: {response.status_code}")
        
        if response.status_code == 200:
            logger.info("Succès! Réponse de l'API:")
            response_json = response.json()
            logger.info(json.dumps(response_json, indent=2))
            return True, json.dumps(response_json, indent=2)
        else:
            logger.error(f"Échec. Réponse de l'API: {response.text}")
            return False, response.text
            
    except Exception as e:
        logger.error(f"Erreur lors de l'appel à l'API: {str(e)}")
        return False, str(e)

def main():
    """
    Fonction principale pour tester les différents formats d'API.
    """
    # Données de test
    movie_data = {
        'movie_id': 4936,
        'movie_name': "The Bank (1915)"
    }
    
    rating_data = {
        'user_id': 5982,
        'movie_id': 4936,
        'rating': 10,
        'timestamp': 1741098588
    }
    
    # Vérifier les arguments
    if len(sys.argv) < 2:
        logger.info("Usage: python test_api.py <format_index>")
        logger.info("format_index doit être entre 1 et 6")
        logger.info("1: Format standard")
        logger.info("2: Seulement l'ID du film")
        logger.info("3: Noms de colonnes exacts")
        logger.info("4: Un seul input avec toutes les données")
        logger.info("5: Noms d'entrée génériques")
        logger.info("6: Format CSV")
        return
    
    try:
        # Récupérer l'index du format à tester
        format_index = int(sys.argv[1])
        
        # Tester le format spécifié
        success, response = test_api_format(format_index, movie_data, rating_data)
        
        # Afficher le résultat final
        if success:
            logger.info(f"Test du format {format_index} réussi!")
        else:
            logger.error(f"Test du format {format_index} échoué.")
            
    except ValueError:
        logger.error("L'index du format doit être un nombre entier")
    except Exception as e:
        logger.error(f"Erreur inattendue: {str(e)}")

if __name__ == "__main__":
    main()
