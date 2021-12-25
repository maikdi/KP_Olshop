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

if __name__ == '__main__':
    app.run(debug=True)