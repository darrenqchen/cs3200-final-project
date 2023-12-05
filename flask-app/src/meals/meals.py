from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


meals = Blueprint('meals', __name__)

# Get meal details from a particular mealID
@meals.route('/meals/<mealID>', methods=['GET'])
def get_meal_detail(mealID):
   query = 'SELECT mealID, name, calories, isVegan, mealTrackerID FROM Meals WHERE mealID = ' + str(mealID)
   current_app.logger.info(query)


   cursor = db.get_db().cursor()
   cursor.execute(query)
   column_headers = [x[0] for x in cursor.description]
   json_data = []
   the_data = cursor.fetchall()
   for row in the_data:
       json_data.append(dict(zip(column_headers, row)))
   return jsonify(json_data)


# Gets a certain ingredient from the DB
@meals.route('/ingredients/<id>', methods=['GET'])
def get_ingredient_detail(id):
   query = 'SELECT ingredientID, name, price, calories, quantity, isVegan FROM Ingredients WHERE ingredientID = ' + str(id)
   current_app.logger.info(query)

   cursor = db.get_db().cursor()
   cursor.execute(query)
   column_headers = [x[0] for x in cursor.description]
   json_data = []
   the_data = cursor.fetchall()
   for row in the_data:
       json_data.append(dict(zip(column_headers, row)))
   return jsonify(json_data)


# TODO fix serializing time and test
# Get a certain recipe
@meals.route('/recipes/<id>', methods=['GET'])
def get_recipe_detail(id):
   query = 'SELECT recipeID, name, rating, servingSize, allergens, calories, timeToMake, steps, isVegan FROM Recipes WHERE recipeID = ' + str(id)
   current_app.logger.info(query)


   cursor = db.get_db().cursor()
   cursor.execute(query)
   column_headers = [x[0] for x in cursor.description]
   json_data = []
   the_data = cursor.fetchall()
   for row in the_data:
       json_data.append(dict(zip(column_headers, row)))
   return jsonify(json_data)


# Deletes a given meal
@meals.route('/meals/<mealID>', methods=['DELETE'])
def delete_meal(mealID):
   query = '''
       DELETE
       FROM Meals
       WHERE mealID = {0};
   '''.format(mealID)
  
   cursor = db.get_db().cursor()
   cursor.execute(query)
  
   db.get_db().commit()
   return "successfully deleted meal #{0}!".format(mealID)


# Deletes a created recipe
@meals.route('/recipes/<id>', methods=['DELETE'])
def delete_recipe(id):
   query = '''
       DELETE
       FROM Recipes
       WHERE recipeID = {0};
   '''.format(id)
  
   cursor = db.get_db().cursor()
   cursor.execute(query)
  
   db.get_db().commit()
   return "successfully deleted recipe #{0}!".format(id)


# Adding a meal
@meals.route('/meals', methods=['POST'])
def add_new_meal():
  
   # collecting data from the request object
   the_data = request.json
   current_app.logger.info(the_data)
#mealID, name, calories, isVegan, mealTrackerID
   #extracting the variable
   name = the_data['name']
   calories = the_data['calories']
   isVegan = the_data['isVegan']
   mealTrackerID = the_data['mealTrackerID']

   # Constructing the query
   query = 'insert into Meals (name, calories, isVegan, mealTrackerID) values ("'
   query += name + '", '
   query += str(calories) + ', '
   query += str(isVegan) + ', '
   query += str(mealTrackerID) + ')'
   current_app.logger.info(query)

   # executing and committing the insert statement
   cursor = db.get_db().cursor()
   cursor.execute(query)
   db.get_db().commit()
  
   return 'Success!'


# Add a new ingredient to DB
@meals.route('/ingredients', methods=['POST'])
def add_new_ingredient():
   # collecting data from the request object
   the_data = request.json
   current_app.logger.info(the_data)

   #extracting the variable
   price = the_data['price']
   quantity = the_data['quantity']
   calories = the_data['calories']
   name = the_data['name']
   isVegan = the_data['isVegan']

   # Constructing the query
   query = 'insert into Ingredients (price, quantity, calories, name, isVegan) values ('
   query += str(price) + ', '
   query += str(quantity) + ', '
   query += str(calories) + ', "'
   query += name + '", '
   query += str(isVegan) + ')'
   current_app.logger.info(query)

   # executing and committing the insert statement
   cursor = db.get_db().cursor()
   cursor.execute(query)
   db.get_db().commit()
  
   return 'Success!'


# Add a new recipe to DB
@meals.route('/recipes', methods=['POST'])
def add_new_recipe():
   # collecting data from the request object
   the_data = request.json
   current_app.logger.info(the_data)

   #extracting the variable
   name = the_data['name']
   rating = the_data['rating']
   servingSize = the_data['servingSize']
   allergens = the_data['allergens']
   calories = the_data['calories']
   timeToMake = the_data['timeToMake']
   steps = the_data['steps']
   isVegan = the_data['isVegan']

   # Constructing the query
   query = 'insert into Recipes (name, rating, servingSize, allergens, calories, timeToMake, steps, isVegan) values ("'
   query += name + '", '
   query += str(rating) + ', '
   query += str(servingSize) + ', "'
   query += allergens + '", '
   query += str(calories) + ', '
   query += str(timeToMake) + ', "'
   query += steps + '", '
   query += str(isVegan) + ')'
   current_app.logger.info(query)

   # executing and committing the insert statement
   cursor = db.get_db().cursor()
   cursor.execute(query)
   db.get_db().commit()
  
   return 'Success!'