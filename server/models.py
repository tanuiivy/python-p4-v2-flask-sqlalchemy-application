from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Contains definitions of tables and associated schema constructs
metadata = MetaData()

# Create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# Define a model class by inheriting from db.Model
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Name cannot be null
    species = db.Column(db.String(100), nullable=False)  # Species cannot be null
    age = db.Column(db.Integer, nullable=False)  # Age is required (you can adjust as needed)

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}, {self.age} years old>'

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
