import os
import pymysql
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Register PyMySQL as a MySQL driver
pymysql.install_as_MySQLdb()

# Charger les variables d'environnement
load_dotenv()

# Configuration de la base de données
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"Tentative de connexion à: {DATABASE_URL}")

# Définition des modèles
Base = declarative_base()

class Prediction(Base):
    __tablename__ = 'predictions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(Integer)
    movie_name = Column(String(255))
    user_id = Column(Integer)
    rating = Column(Float)
    timestamp = Column(Integer)
    prediction = Column(Float)
    prediction_timestamp = Column(DateTime)

class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

# Données d'exemple de films
SAMPLE_MOVIES = [
    {"id": 91, "name": "Le manoir du diable (1896)"},
    {"id": 4936, "name": "The Bank (1915)"},
    {"id": 6684, "name": "The Fireman (1916)"},
    {"id": 9968, "name": "Broken Blossoms or The Yellow Man and the Girl (1919)"},
    {"id": 10247, "name": "Herr Arnes pengar (1919)"},
    {"id": 11267, "name": "Headin Home (1920)"}
]

try:
    # Création du moteur SQLAlchemy
    engine = create_engine(DATABASE_URL)
    print("Moteur SQLAlchemy créé avec succès")
    
    # Création des tables
    Base.metadata.create_all(engine)
    print("Tables créées avec succès")
    
    # Ajout des films d'exemple
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Vérifier si la table movies est vide
    movie_count = session.query(Movie).count()
    print(f"Nombre de films dans la base de données: {movie_count}")
    
    if movie_count == 0:
        print("Ajout des films d'exemple...")
        # Ajouter les films d'exemple
        for movie in SAMPLE_MOVIES:
            session.add(Movie(id=movie["id"], name=movie["name"]))
        session.commit()
        print(f"{len(SAMPLE_MOVIES)} films ajoutés avec succès")
    
    session.close()
    print("Initialisation de la base de données terminée avec succès")
    
except Exception as e:
    print(f"Erreur lors de l'initialisation de la base de données: {e}")
