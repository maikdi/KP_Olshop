from flask import Flask, request, jsonify
from sql_connector import DB
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
shop_database = DB()

@app.route("/login", methods=["POST"])
def login():
	json_data = request.get_json()
	username = json_data["username"]
	password = json_data["password"]
	get_user = shop_database.select_id_pass(username,password)
	print(username)
	if len(get_user) == 0:
		response = {
			"response" : "Not Valid"
		}
		return jsonify(response)
	else:
		# session['role'] = get_user[0][2]
		response = {
			"response" : "Valid"
		}
		return jsonify(response)

@app.route("/get_dashboard", methods=["GET"])
def get_all_products():
	all_products = shop_database.get_all_products() #List of tuple e.g: [('id', 'name', 'price), ('id2', 'name2', 'price2'), ...]
	data = {"data" : all_products}
	return jsonify(data)
app.run()