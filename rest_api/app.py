from flask import Flask, request, jsonify
from sql_connector import DB
from flask_cors import CORS
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '../src/assets/'
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
	get_admin = shop_database.select_from_admin(username, password)
	# print(username)
	if len(get_user) == 0:
		if len(get_admin) == 0:
			response = {
				"response" : "Not Valid"
			}
			return jsonify(response)
		else:
			# session['role'] = get_user[0][2]
			response = {
				"response" : "Admin"
			}
			return jsonify(response)
	else:
		response = {
				"response" : "User"
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

@app.route("/cancel-all" , methods=["POST"])
def cancel_all():	
	json_data = request.get_json()
	user = json_data['user']
	user = shop_database.find_username(user)[0]
	invoice_id = user[1] + "_" + str(user[-1])
	shop_database.delete_invoice(invoice_id)
	data = {"Response" : "OK"}
	return jsonify(data)

@app.route("/update-product", methods=["POST"])
def update_product():
	json_data = request.get_json()
	data = json_data['data']
	prod_id = data[0]
	new_name = data[1]
	new_price = data[2]
	new_category = data[3]
	new_desc = data[4]
	new_img_path = data[5]
	shop_database.update_product(prod_id, new_name, new_price, new_category, new_desc, new_img_path)
	data = {"Response" : "OK"}
	return jsonify(data)

@app.route("/update-image", methods=["POST"])
def update_image():
	try:
		print("Image Uploaded")
		image = request.files['image_file']
		img_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
		image.save(img_path)
	except:
		print("Upload Fail")
		pass

	data = {"Response" : "OK"}
	return jsonify(data)

@app.route("/delete-product", methods=["POST"])
def delete_product():
	json_data = request.get_json()
	product_id = json_data['data']
	shop_database.delete_product(product_id)
	data = {"Response" : "OK"}
	return jsonify(data)

@app.route('/add-product', methods=["POST"])
def add_product():
	data = request.get_json()
	new_name = data['name']
	new_price = data['price']
	new_category = data['category']
	new_desc = data['description']
	new_img_path = data['image_name']
	print(new_img_path)
	shop_database.add_product(new_name, new_price, new_category, new_desc, new_img_path)
	data = {"Response" : "OK"}
	return jsonify(data)

@app.route("/get-sale-report", methods=["GET"])
def get_sale_report():
	all_sales = shop_database.get_sales()
	all_product_sales = []
	for sales in all_sales:
		query = shop_database.get_invoices_by_id(sales[0])
		all_product_sales.extend(query)
	data = {
		"all_sales" : all_sales,
		"all_product_sales" : all_product_sales
		}
	return jsonify(data)

app.run(debug=True)
