from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime, inspect, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import pymysql

# Register PyMySQL as a MySQL driver
pymysql.install_as_MySQLdb()

# Charger les variables d'environnement
load_dotenv()

# Configuration de la base de données
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

def check_table_structure():
    """Vérifie la structure actuelle de la table predictions"""
    inspector = inspect(engine)
    
    print("Tables dans la base de données:")
    print(inspector.get_table_names())
    
    if 'predictions' in inspector.get_table_names():
        print("\nColonnes dans la table 'predictions':")
        for column in inspector.get_columns('predictions'):
            print(f"- {column['name']} ({column['type']})")
    else:
        print("\nLa table 'predictions' n'existe pas.")

def update_table_structure():
    """Met à jour la structure de la table predictions si nécessaire"""
    inspector = inspect(engine)
    
    if 'predictions' in inspector.get_table_names():
        columns = [column['name'] for column in inspector.get_columns('predictions')]
        
        # Vérifier si les colonnes nécessaires existent
        missing_columns = []
        if 'movie_id_pred' not in columns:
            missing_columns.append("ADD COLUMN movie_id_pred FLOAT")
        
        # Ajouter les colonnes manquantes
        if missing_columns:
            with engine.connect() as connection:
                for column_def in missing_columns:
                    alter_query = f"ALTER TABLE predictions {column_def}"
                    print(f"Exécution de: {alter_query}")
                    connection.execute(text(alter_query))
                connection.commit()
                print("Structure de la table mise à jour avec succès.")
        else:
            print("La structure de la table est déjà à jour.")
    else:
        # Créer la table si elle n'existe pas
        metadata = MetaData()
        predictions = Table(
            'predictions', metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('movie_id', Integer),
            Column('movie_name', String(255)),
            Column('user_id', Float),
            Column('movie_id_pred', Float),
            Column('rating', Float),
            Column('timestamp', Float),
            Column('prediction_timestamp', DateTime)
        )
        metadata.create_all(engine)
        print("Table 'predictions' créée avec succès.")

if __name__ == "__main__":
    print("Vérification de la structure de la base de données...")
    check_table_structure()
    
    print("\nMise à jour de la structure de la base de données...")
    update_table_structure()
    
    print("\nStructure finale de la base de données:")
    check_table_structure()
