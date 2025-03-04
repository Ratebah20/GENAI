# TP : Création et Déploiement d'un Modèle de Machine Learning sur Azure avec Sécurité et Haute Disponibilité

## Objectifs du TP :

 - Créer et entraîner un modèle de Machine Learning sur Azure.
 - Déployer une application web pour tester le modèle depuis une VM Azure.
 - Mettre en place une infrastructure sécurisée et hautement disponible sur Azure.

### 1) Création et Entraînement du Modèle de Machine Learning
A) Utiliser Azure Machine Learning Studio pour créer et entraîner un modèle prédictif,
Création de workplace pour machine learning 

![image](https://github.com/user-attachments/assets/b59027d8-2b2a-4385-9904-16602e864493)
![image](https://github.com/user-attachments/assets/144dba02-0303-4c60-9893-e2d81f4a23bc)

après le déploiement on se rend dans la section concepteur 
![image](https://github.com/user-attachments/assets/4c315b07-dc6a-4ac0-bc01-50f356968ed0)

 on ajoute notre DataSet 
![image](https://github.com/user-attachments/assets/72a5dbfd-7f0a-46ff-bdb8-297b41460682)
movie_titles contient le ID et NOM des films, on ajoute aussi movie_rating pour avoir des données pertinents pour notre test
movie_rating:
![image](https://github.com/user-attachments/assets/199d4bb1-aeb6-492a-9cca-6bedc583826a)
movie_title:
![image](https://github.com/user-attachments/assets/42877532-17d7-41ce-b892-b260ca64d432)
Ensuite on fait un jointure entre movie_rating et movie_title avec le ID movie qui est la clé étranger dans movie_rating et clé primaire dans movie_title

Puis on doit choisir les données pour le traitement
![image](https://github.com/user-attachments/assets/8ff2e5ef-c234-4a95-a822-48881f0f6a7b)
on oublie pas d'ajouter le moive name
![image](https://github.com/user-attachments/assets/81e32084-4a79-4263-8ded-5320ede68934)
Par la suite on nettoie les données 
![image](https://github.com/user-attachments/assets/b3e1b092-1dcb-440e-966a-1cd700d69b8d)
![image](https://github.com/user-attachments/assets/a6a6cc1f-02cf-4fb3-9f3e-c61cbffdc63f)
On normalise les données 
![image](https://github.com/user-attachments/assets/2cbe41a5-4825-42a5-8592-d70a3ede535c)
![image](https://github.com/user-attachments/assets/8879a981-fbbe-4f04-9bff-10b2cddf94e8)
également on ajoute un split data avec ces données : 
![image](https://github.com/user-attachments/assets/82757a75-6ff5-4dec-a24f-46a1d9d02ad2)
ensuite on choisir le champ qui nous intéresse, ici on choisira le rank des films 
![image](https://github.com/user-attachments/assets/7f982b18-bf34-4327-94c1-2fb67ddd37a5)
de plus il faut ajouter le linera regression 
![image](https://github.com/user-attachments/assets/fae8c58f-e1f3-4179-b986-45f3bc5159b1)
il faudra aussi ajouter score model et evaluate model pour évaluer notre RSE 
![image](https://github.com/user-attachments/assets/1f4dbf32-3f58-42c8-bcbc-945dea5f9c98)

### Une fois que notre pipeline configuré on crée un cluster
![image](https://github.com/user-attachments/assets/096d58d5-e036-4079-ae6d-d56d6f8ca9b7)
![image](https://github.com/user-attachments/assets/4c1dc20e-e987-4dfc-b1ee-b6edf2006441)
Par la suite on configure notre expérience et en envoie 
![image](https://github.com/user-attachments/assets/fd719726-ecf7-4ba6-b484-b781b617f9a5)

Voilà le résultat 
![image](https://github.com/user-attachments/assets/18a5c07a-c904-41f9-83bf-58adbe77f3fe)
on oublie pas de vérifier le RSE 
![image](https://github.com/user-attachments/assets/8e447639-adff-4594-84f2-8eb981c651df)
résultat des données  
![image](https://github.com/user-attachments/assets/f42696fb-0ade-4ce9-a9db-0f998a117218)

### Une fois que tout est fonctionnel, on crée le inférence en temps réel et on lance l'expérience
![image](https://github.com/user-attachments/assets/dec1d07f-dda6-40a6-8baa-1a9ffb6bf6a3)
![image](https://github.com/user-attachments/assets/3697cc99-5316-4c09-8e57-af05c41c0f58)
après on va déployer le pipeline
![image](https://github.com/user-attachments/assets/bd17f168-7d00-45d2-8353-e6b042c27ad5)
après le deploiement 
![image](https://github.com/user-attachments/assets/afcd0fdf-d98a-40d1-8e90-68dc484cecd1)
dans la section consumer on trouve les credentials pour utiliser notre API REST
![image](https://github.com/user-attachments/assets/31c61af3-fbe4-40b8-b8ae-3b640697a22d)

## Déploiement de l'Infrastructure sur Azure
1 Configurer et déployer une machine virtuelle (VM) sur Azure
on entre les information de base et laisse les autre champ par défaut
![image](https://github.com/user-attachments/assets/cab4fd20-729d-490d-a3f5-6de1382cd23c)
![image](https://github.com/user-attachments/assets/613a319d-eaca-4869-b7ed-7370268da3e9)
ensuie on télécharge le fichier RDP pour se connecter à la VM
![image](https://github.com/user-attachments/assets/28a0e906-7f7a-415b-9554-9108e1386b44)
![image](https://github.com/user-attachments/assets/847ad39f-36ab-474f-89aa-320161bdf8ec)

### Installer les outils nécessaires pour déployer et tester le modèle de Machine Learning sur la VM
Une fois connecté à la VM on install postman 
![image](https://github.com/user-attachments/assets/dc688149-2952-4d30-bfd9-249fb7e567af)
On entre notre URL API
![image](https://github.com/user-attachments/assets/d80d1dd8-0a65-46d3-8402-ca423275b1e6)
On ajoute notre bearer token 
![image](https://github.com/user-attachments/assets/5cf2dfef-25bf-4284-8bae-9184f4bc33bb)
on doit intéroger notre API en envoyant des données dans le corps avec ces données,
le format doit être en json
![image](https://github.com/user-attachments/assets/b14691fc-51b5-4484-ac2c-41ab2e10526c)
on reçoit la réponse avec un code 200 et le résultat 
![image](https://github.com/user-attachments/assets/80b328f6-71ad-46f7-800c-718336809a0b)

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

Contient le URL de la DB

### Configuration de l'API Azure ML

```python
AZURE_ML_ENDPOINT = "http://868c7bfc-60e0-4ecb-aa6a-ae0403081c17.francecentral.azurecontainer.io/score"
API_KEY = "ici on doit mettre le api key"
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
   - Créer une base de données MySQL nommée `tpia`
   - Configurer les variables d'environnement dans le fichier `.env`
   - Exécuter le script d'initialisation :
     ```
     python init_db.py
     ```

4. Démarrer l'application :
   ```
   python app.py
   ```

5. Accéder à l'application dans le navigateur :
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

## Héberger l'application sur une VM Azure et s'assurer qu'elle peut recevoir des requêtes et retourner des prédictions
Pour héberger notre applcation on doit d'abord push mon projet dans git repo
Pour cela j'ai crée un nouveau repository avec le nom GENAI
Et le configurer ainsi 
![image](https://github.com/user-attachments/assets/6fdbd08a-ce6a-4256-b808-aa42747f15a8)
![image](https://github.com/user-attachments/assets/db1264ca-3f58-4e35-b54d-1f5943d6941e)
![image](https://github.com/user-attachments/assets/b692c0b2-ca4e-476d-81b8-11f26db8dc84)
Je viens de push mon projet sur github 
![image](https://github.com/user-attachments/assets/de3910f3-180b-4944-9509-7d50e13b57d2)

### Ensuite on se rend sur la machine virtuel et on install vs code
![image](https://github.com/user-attachments/assets/5bacdf15-badd-4d4e-b68d-dfda16e52187)
puis on install git
![image](https://github.com/user-attachments/assets/f892d49a-b8f6-4b78-932c-062a3a465e81)
cela nous permet de faire un git clone pour pull notre projet dans la VM
![image](https://github.com/user-attachments/assets/72665fb5-87f7-4eaa-b616-8b5b6523e760)
notre projet a bien été pull
![image](https://github.com/user-attachments/assets/822b7616-bae7-4734-adec-5ed6d045e777)
ensuite on install python 
![image](https://github.com/user-attachments/assets/0684c400-6148-44b9-9328-0f537b042d97)
puis wmap server pour notre server mysql
![image](https://github.com/user-attachments/assets/7f7119a6-4df4-4e41-bb91-0d2cbcd4416d)
une fois wamp installé on doit crée un DB avec le nom tpia
![image](https://github.com/user-attachments/assets/d3297566-986f-4656-b7b0-bb06756c84fc)
![image](https://github.com/user-attachments/assets/d019d545-77c8-4e17-83ae-894312732691)
une fois la DB crée on lance la migration de nos tables 
![image](https://github.com/user-attachments/assets/90496128-c83f-4611-9354-cac17f1c5c4d)
![image](https://github.com/user-attachments/assets/ec866904-3c6a-4184-842b-eedf68f0b381)
On doit aussi tester notre API pour voir si il est fonctionnel et qu'il accepte les données envoyés
![image](https://github.com/user-attachments/assets/5e93f8b7-4488-40cd-8695-32bc1e3438a2)
![image](https://github.com/user-attachments/assets/134e353f-5cb3-4e4d-87de-e9d640827db1)
Une fois le teste réussi on peut lancer notre serveur flask pour tester via le frond end
![image](https://github.com/user-attachments/assets/83ccfc15-bd11-40d4-bd82-a60948e2427d)
![image](https://github.com/user-attachments/assets/cc181ab1-b540-4db4-a1d9-be2aacd2d61e)
grâce au menu déroulant l'utilisateur peut choisir le film souhaité 
![image](https://github.com/user-attachments/assets/d04c93c4-1bc8-41a2-8ceb-a8d0c1b98dc8)
![image](https://github.com/user-attachments/assets/b96abcf6-6d99-45be-9d12-1fa791e43302)
on peut voir le résultat dans le console 
![image](https://github.com/user-attachments/assets/a53fd6fe-cca4-4d8d-b040-184adaa5645c)
preuve de réussite 
![image](https://github.com/user-attachments/assets/aaf7656f-35c4-4ed7-8b63-adfffd4e12c7)

il nous reste une dernière étape et de vérifier la BD
La migration effectué précédemment a permit de créer ces deux tables
![image](https://github.com/user-attachments/assets/d3785113-1cd9-4088-8739-78a7cb5e5fd5)
les données 
![image](https://github.com/user-attachments/assets/7bc7feed-047d-42e8-8533-48c59ec22de7)
les données de prédiction ont été ajouter avec succes dans la BD
![image](https://github.com/user-attachments/assets/c5bb08d1-3803-43d5-b5b5-ff6a5e1eab57)





















