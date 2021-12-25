import mysql.connector

class DB:
    def __init__(self):
        dbconfig = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'uas_web'
        }
        self.conn = mysql.connector.connect(**dbconfig)
        self.cursor = self.conn.cursor()
    
    def select_id_pass(self, username, password):
        select_statement = """
        SELECT * FROM users
        WHERE username = %s AND password = %s;
        """
        self.cursor.execute(select_statement, (username, password,))
        user = self.cursor.fetchall()
        return user

    def insert_user(self, first_name, last_name, username, password):
        insert_statement = f"INSERT INTO users (first_name, last_name, username, password) VALUES ('{first_name}', '{last_name}', '{username}' ,'{password}')"
        self.cursor.execute(insert_statement)
        self.conn.commit()
        
    def find_username(self, username):
        select_statement = "SELECT * FROM users WHERE username = %s;"
        self.cursor.execute(select_statement, (username,))
        user = self.cursor.fetchall()
        print(user)
        return user
    
    def get_all_products(self):
        select_statement = """
        SELECT * FROM product;
        """
        self.cursor.execute(select_statement)
        all_products = self.cursor.fetchall()
        return all_products #(id, name, price, kategori, deskripsi, path)

