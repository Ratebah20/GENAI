# Système de Prédiction de Notes de Films

## Aperçu du Projet

Ce projet est une application web qui prédit les notes de films en utilisant un modèle d'apprentissage automatique hébergé sur Azure Machine Learning. L'application permet aux utilisateurs de sélectionner un film et d'obtenir une prédiction de la note que ce film pourrait recevoir, basée sur des données historiques de notation.

## Fonctionnalités Principales

- Sélection de films à partir d'une base de données MySQL
- Prédiction de notes de films via une API Azure Machine Learning
- Mécanisme de fallback avec simulation de prédiction en cas d'échec de l'API
- Stockage des prédictions dans une base de données pour analyse ultérieure
- Interface utilisateur intuitive pour la sélection de films et l'affichage des résultats

## Architecture Technique

### Stack Technologique

- **Backend** : Python 3.x avec Flask
- **Frontend** : HTML, CSS, JavaScript
- **Base de données** : MySQL
- **ORM** : SQLAlchemy
- **API ML** : Azure Machine Learning
- **Autres bibliothèques** : Pandas, Requests, PyMySQL, python-dotenv

### Structure du Projet

```
mon_projet/
│
├── app.py                 # Application principale Flask
├── data_converter.py      # Convertisseur de données pour l'API Azure ML
├── init_db.py             # Script d'initialisation de la base de données
├── update_db.py           # Script de mise à jour de la base de données
├── test_api.py            # Outil de test pour l'API Azure ML
├── .env                   # Fichier de configuration (variables d'environnement)
│
├── static/
│   ├── styles.css         # Styles CSS
│   └── script.js          # JavaScript pour l'interaction utilisateur
│
└── templates/
    └── index.html         # Template HTML principal
```

## Fonctionnement Détaillé

### 1. Initialisation de la Base de Données

Le script `init_db.py` crée les tables nécessaires dans la base de données MySQL :
- `movies` : Stocke les informations sur les films (ID, titre)
- `predictions` : Stocke les prédictions générées (film, utilisateur, note prédite, date)

### 2. Processus de Prédiction

1. **Sélection du Film** : L'utilisateur sélectionne un film dans l'interface web
2. **Préparation des Données** :
   - Les données du film (ID, nom) sont extraites
   - Des valeurs sont générées pour l'utilisateur (ID, note, timestamp)
   - Les données sont formatées selon le schéma attendu par l'API Azure ML

3. **Appel à l'API Azure ML** :
   - Les données sont envoyées à l'API via une requête POST
   - Le format spécifique utilisé est crucial pour le bon fonctionnement :
     ```json
     {
       "Inputs": {
         "WebServiceInput0": [
           {
             "UserId": 5982,
             "MovieId": 4936,
             "Rating": 10,
             "Timestamp": 1741098588
           }
         ],
         "WebServiceInput1": [
           {
             "Movie ID": 4936,
             "Movie Name": "The Bank (1915)"
           }
         ]
       }
     }
     ```

4. **Traitement de la Réponse** :
   - Si l'API répond avec succès (code 200), la prédiction est extraite
   - Si l'API échoue, le système bascule vers un mode de simulation

5. **Stockage des Résultats** :
   - La prédiction est stockée dans la base de données
   - Les détails sont affichés à l'utilisateur

### 3. Conversion des Données

Le module `data_converter.py` est responsable de la transformation des données au format attendu par l'API Azure ML. Il gère :
- La conversion des types de données
- La structure JSON spécifique
- Le nommage précis des champs

### 4. Test de l'API

L'outil `test_api.py` permet de tester individuellement différents formats de données avec l'API Azure ML pour identifier celui qui fonctionne. Il prend en charge :
- 6 formats différents de données
- L'affichage détaillé des requêtes et réponses
- La journalisation des résultats

## Configuration

### Variables d'Environnement (.env)

URL de la DB

### Configuration de l'API Azure ML

```python
AZURE_ML_ENDPOINT = "http://868c7bfc-60e0-4ecb-aa6a-ae0403081c17.francecentral.azurecontainer.io/score"
API_KEY = "mon_api_key"
```

## Installation et Démarrage

### Prérequis

- Python 3.x
- MySQL Server
- Pip (gestionnaire de paquets Python)

### Installation

1. Cloner le dépôt :
   ```
   git clone <url-du-depot>
   cd mon_projet
   ```

2. Installer les dépendances :
   ```
   pip install -r requirements.txt
   ```

3. Configurer la base de données :
   - Créer une base de données MySQL nommée `movie_ratings`
   - Configurer les variables d'environnement dans le fichier `.env`
   - Exécuter le script d'initialisation :
     ```
     python init_db.py
     ```

4. Démarrer l'application :
   ```
   python app.py
   ```

5. Accéder à l'application dans votre navigateur :
   ```
   http://localhost:5000
   ```

## Dépannage et Développement

### Test de l'API

Pour tester différents formats d'envoi de données à l'API :

```
python test_api.py <format_index>
```

Où `<format_index>` est un nombre entre 1 et 6 correspondant aux différents formats implémentés.

### Journalisation

L'application utilise le module de journalisation Python pour enregistrer les informations importantes :
- Requêtes et réponses de l'API
- Erreurs et exceptions
- Conversions de données


## Technique Utilisée

1. **Format de Données Complexe** : L'API Azure ML nécessite un format de données précis avec des noms de champs spécifiques et une structure JSON particulière.

2. **Inversion des Inputs** : La résolution d'un problème majeur a été l'inversion des inputs dans la requête API :
   - WebServiceInput0 doit contenir les données de notation (UserId, MovieId, Rating, Timestamp)
   - WebServiceInput1 doit contenir les données du film (Movie ID, Movie Name)

3. **Conversion des Types** : Les types de données doivent être strictement respectés (entiers pour les IDs et les notes).

4. **Gestion des Erreurs** : Mise en place d'un système robuste de fallback en cas d'échec de l'API.


