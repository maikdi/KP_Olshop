from flask import Flask, request, jsonify
from sql_connector import DB
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
shop_database = DB()

# @app.route("/", methods=["POST"])
# def add_to_cart():
# 	pass

@app.route("/login", methods=["POST"])
def login():
	json_data = request.get_json()
	username = json_data["username"]
	password = json_data["password"]
	get_user = shop_database.select_id_pass(username, password)
	# print(username)
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

@app.route('/sign-up', methods=['POST'])
def sign_up():
	json_data = request.get_json()
	first_name = json_data['first_name']
	last_name = json_data['last_name']
	username = json_data['username']
	password = json_data['password']

	if (username and password != ""): 
		if len(shop_database.find_username(username)) == 0:
			shop_database.insert_user(first_name, last_name, username, password)
			result = {
				'data': {
					'first name': first_name,
					'last name': last_name,
					'username': username,
					'password': password
				},
				'response': 'valid'
			}
		else:
			result = {'response': 'username taken'}
	elif (username == "") & (password != ""):
		result = {'response': 'username blank'}
	elif (username != "") & (password == ""):
		result = {'response': 'password blank'}
	else:
		result = {'response': 'required field'}
	return jsonify(result)

@app.route("/get_dashboard", methods=["GET"])
def get_all_products():
	all_products = shop_database.get_all_products() #List of tuple e.g: [('id', 'name', 'price), ('id2', 'name2', 'price2'), ...]
	data = {"data" : all_products}
	return jsonify(data)

@app.route("/add-cart", methods=["PUT"])
def add_to_cart():
	json_data = request.get_json()
	data = json_data['cart']
	user = json_data['user']
	user = shop_database.find_username(user)[0]
	user_id = user[0]
	invoice_id = user[1] + "_" + str(user[-1])
	for items in data:
		shop_database.add_invoice(invoice_id, user_id, items[0])
	response = {
			"response" : "Succesfull"
		}
	return jsonify(response)
@app.route("/get-cart", methods=["POST"])
def get_cart():
	json_data = request.get_json()
	user = json_data['user']
	user = shop_database.find_username(user)[0]
	invoice_id = user[1] + "_" + str(user[-1])
	data = {"data" : shop_database.get_current_user_invoice(invoice_id)}
	return jsonify(data)

@app.route("/cancel-item", methods=["POST"])
def cancel_item():
	json_data = request.get_json()
	user = json_data['user']
	product_id = json_data['product_id']
	user = shop_database.find_username(user)[0]
	invoice_id = user[1] + "_" + str(user[-1])
	shop_database.delete_item(invoice_id, product_id)
	data = {"Response" : "OK"}
	return jsonify(data)

@app.route("/minus-quantity", methods=["PUT"])
def minus_quantity():
	json_data = request.get_json()
	user = json_data['user']
	product_id = json_data['product_id']
	user = shop_database.find_username(user)[0]
	invoice_id = user[1] + "_" + str(user[-1])
	shop_database.minus_quantity(invoice_id, product_id)
	data = {"Response" : "OK"}
	return jsonify(data)

@app.route("/plus-quantity", methods=["PUT"])
def plus_quantity():
	json_data = request.get_json()
	user = json_data['user']
	product_id = json_data['product_id']
	user = shop_database.find_username(user)[0]
	invoice_id = user[1] + "_" + str(user[-1])
	shop_database.plus_quantity(invoice_id, product_id)
	data = {"Response" : "OK"}
	return jsonify(data)

@app.route("/checkout", methods=["POST"])
def checkout():
	json_data = request.get_json()
	user = json_data['user']
	total = json_data['total']
	date = json_data['date']
	user = shop_database.find_username(user)[0]
	invoice_id = user[1] + "_" + str(user[-1])
	shop_database.add_sales(invoice_id, total, date)
	shop_database.increase_user_invoice_id(user[0])
	data = {"Response" : "OK"}
	return jsonify(data)

@app.route('/admin', methods=["POST"])
def add_product():
	pass

app.run(debug=True)
