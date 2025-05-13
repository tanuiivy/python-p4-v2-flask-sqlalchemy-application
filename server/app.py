#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, render_template
from flask_migrate import Migrate

from models import db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Home Route (Root)
@app.route('/')
def home():
    return "Welcome to the Pet Database!"

# Route to get all pets
@app.route('/pets', methods=['GET'])
def get_pets():
    pets = Pet.query.all()  # Query all Pet records
    pets_data = [{"id": pet.id, "name": pet.name, "age": pet.age} for pet in pets]
    return jsonify(pets_data)

# Route to get a pet by id
@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)  # Fetch a pet by id or return 404 if not found
    pet_data = {"id": pet.id, "name": pet.name, "age": pet.age}
    return jsonify(pet_data)

# Route to create a new pet (POST)
@app.route('/pets', methods=['POST'])
def create_pet():
    # For simplicity, let's assume you're passing data directly in the request
    pet_name = request.json.get('name')
    pet_age = request.json.get('age')
    
    # Create and add the new pet to the database
    new_pet = Pet(name=pet_name, age=pet_age)
    db.session.add(new_pet)
    db.session.commit()
    
    return jsonify({"message": "Pet created successfully!"}), 201

# Route to update a pet (PUT)
@app.route('/pets/<int:pet_id>', methods=['PUT'])
def update_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    
    pet.name = request.json.get('name', pet.name)
    pet.age = request.json.get('age', pet.age)
    
    db.session.commit()
    
    return jsonify({"message": "Pet updated successfully!"})

# Route to delete a pet
@app.route('/pets/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    
    return jsonify({"message": "Pet deleted successfully!"})

if __name__ == '__main__':
    app.run(port=5555, debug=True)

