from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from celery import Celery
from sql_connector import DB
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '../src/assets/'
app.config['SECRET_KEY'] = 'IBDA3211-Sistem Terdistribusi-Michael-191900564'
# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'INSERT VALID EMAIL HERE'
app.config['MAIL_PASSWORD'] = 'INSER VALID PASSWORD HERE'
app.config['MAIL_DEFAULT_SENDER'] = 'INSERT ANOTHER VALID EMAIL HERE'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

CORS(app)
shop_database = DB()

# Initialize extensions
mail = Mail(app)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def send_async_email(email_data):
    msg = Message(email_data["subject"], sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[email_data['to']])
    msg.body = email_data['body']
    mail.send(msg)
    return "Async Email Sending Success"

@app.route('/send_mail', methods=["POST"])
def send_mail():
	email_data = request.get_json()	
	print(email_data)
	receiver = email_data['to']
	if receiver == "all":
		all_receiver = shop_database.get_all_user_email()
		for receivers in all_receiver:
			print(receivers[0])
			message = {
				"subject" : email_data['subject'],
				"to" : 	receivers[0],
				"body" : email_data['body'],
			}
			send_async_email(message)
	else:
		message = {
				"subject" : email_data['subject'],
				"to" : 	shop_database.get_user_email_by_username(receiver)[0][0],
				"body" : email_data['body']
			}
		print(message['to'])
		send_async_email(message)
	return "Email delivered"

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
	email = json_data['email']

	if (username and password != ""): 
		if len(shop_database.find_username(username)) == 0:
			shop_database.insert_user(first_name, last_name, username, password, email)
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

@app.route("/search-product", methods=["POST"])
def search_product():
	keyword = request.get_json()
	all_products = shop_database.search_product(keyword) #List of tuple e.g: [('id', 'name', 'price), ('id2', 'name2', 'price2'), ...]
	data = {"data" : all_products}
	return jsonify(data)


@app.route("/search-sale", methods=["POST"])
def search_sale():
	json_data = request.get_json()
	start_date = json_data['startDate']
	end_date = json_data['endDate']
	if ((start_date != "") and (end_date != "")):
		all_sales = shop_database.get_sales_by_date(start_date, end_date)
		all_product_sales = []
		for sales in all_sales:
			query = shop_database.get_invoices_by_id(sales[0])
			all_product_sales.extend(query)
		data = {
			"all_sales" : all_sales,
			"all_product_sales" : all_product_sales
			}
		return jsonify(data)
	elif ((start_date == "") and (end_date != "")):
		start_date = "0000-01-01"
		all_sales = shop_database.get_sales_by_date(start_date, end_date)
		all_product_sales = []
		for sales in all_sales:
			query = shop_database.get_invoices_by_id(sales[0])
			all_product_sales.extend(query)
		data = {
			"all_sales" : all_sales,
			"all_product_sales" : all_product_sales
			}
		return jsonify(data)

	elif ((start_date != "") and (end_date == "")):
		end_date = "9999-12-31"
		all_sales = shop_database.get_sales_by_date(start_date, end_date)
		all_product_sales = []
		for sales in all_sales:
			query = shop_database.get_invoices_by_id(sales[0])
			all_product_sales.extend(query)
		data = {
			"all_sales" : all_sales,
			"all_product_sales" : all_product_sales
			}
		return jsonify(data)
	else:
		return get_sale_report()

app.run(debug=True)
