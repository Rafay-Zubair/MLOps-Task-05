from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connection with MongoDB
db_client = MongoClient(os.environ.get('HOST_URL'), int(os.environ.get('DB_PORT')))
# Database
db = db_client.user_data
# Collection
doc_collection = db.users

# if doc_collection.count_documents({}) == 0:
# 	# When doctors collection is empty
# 	doctors = [
# 		{ 'id': "1",'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality' : "DevOps"  },
# 		{ 'id': "2",'firstName': "Good", 'lastName': "Doctor",'speciality' : "Test"  }
# 	]	
# 	for doctor in doctors:
# 		doc_collection.insert_one(doctor)


@app.route('/hello')
def hello():
	greeting = "Hello world!"
	return greeting

@app.route('/adduser', methods=["POST"])
def insertUser():
  userName = request.form.get('username')
  email = request.form.get('email')
  
  doc_collection.insert_one({ 'uesrname':userName, 'email':email })
  
  return "Data Added"

@app.route('/users', methods=["GET"])
def getAllUsers():
	data = list(doc_collection.find())
	for d in data:
		d.pop("_id")
	return jsonify(data)



if __name__ == "__main__":
	app.run(host="0.0.0.0",port=9090)

