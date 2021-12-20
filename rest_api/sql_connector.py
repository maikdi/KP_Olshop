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
    def select_id_pass(self,username, password):
        select_statement = """
        SELECT * FROM users
        WHERE username = %s AND password = %s;
        """
        self.cursor.execute(select_statement, (username,password,))
        user = self.cursor.fetchall()
        return user
    
    def get_all_products(self):
        select_statement = """
        SELECT id, name, price FROM product;
        """
        self.cursor.execute(select_statement)
        all_products = self.cursor.fetchall()
        return all_products
