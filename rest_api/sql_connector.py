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

    def select_from_admin(self, username, password):
        select_statement = """
        SELECT * FROM admins
        WHERE username = %s AND password = %s;
        """
        self.cursor.execute(select_statement, (username, password,))
        user = self.cursor.fetchall()
        return user

    def insert_user(self, first_name, last_name, username, password, email):
        insert_statement = f"INSERT INTO users (first_name, last_name, username, password, email) VALUES ('{first_name}', '{last_name}', '{username}' ,'{password}' , '{email}')"
        self.cursor.execute(insert_statement)
        self.conn.commit()
        
    def find_username(self, username):
        select_statement = "SELECT * FROM users WHERE username = %s;"
        self.cursor.execute(select_statement, (username,))
        user = self.cursor.fetchall()
        return user
    
    def get_all_products(self):
        select_statement = """
        SELECT * FROM product;
        """
        self.cursor.execute(select_statement)
        all_products = self.cursor.fetchall()
        return all_products #(id, name, price, kategori, deskripsi, path)

    def search_invoice_duplicate_item(self, invoice_id, product_id):
        select_statement = """
        SELECT * FROM invoices
        WHERE invoice_id = %s AND product_id = %s;
        """
        self.cursor.execute(select_statement, (invoice_id, product_id, ))
        product = self.cursor.fetchall()
        return product

    def add_invoice(self, invoice_id, user_id, product_id):
        item_in_invoice = self.search_invoice_duplicate_item(invoice_id, product_id)
        if len(item_in_invoice) == 0:
            insert_statement = """
            INSERT INTO invoices 
            (invoice_id, user_id, product_id, quantity)
            VALUES (%s, %s, %s, 1);
            """
            self.cursor.execute(insert_statement, (invoice_id, user_id, product_id, ))

        else:
            update_statement = """
            UPDATE invoices
            SET quantity = quantity + 1
            WHERE invoice_id = %s AND user_id = %s AND product_id = %s
            """
            self.cursor.execute(update_statement, (invoice_id, user_id, product_id, ))
        self.conn.commit()

    def get_current_user_invoice(self, invoice_id):
        select_statement = """
        SELECT `product`.`name`, `product`.`price`, `product`.`path`, `invoices`.`quantity`,  `invoices`.`product_id`
        FROM `invoices`
        INNER JOIN `product` on `invoices`.`product_id` = `product`.`id`
        WHERE `invoice_id` = %s
        """
        self.cursor.execute(select_statement, (invoice_id, ))
        cart = self.cursor.fetchall()
        return cart

    def delete_item(self, invoice_id, product_id):
        delete_statement = """
        DELETE FROM `invoices` WHERE `invoice_id` = %s AND `product_id` = %s
        """
        self.cursor.execute(delete_statement, (invoice_id, product_id, ))
        self.conn.commit()

    def minus_quantity(self, invoice_id, product_id):
        update_statement = """
            UPDATE invoices
            SET quantity = quantity - 1
            WHERE invoice_id = %s AND product_id = %s
            """
        self.cursor.execute(update_statement, (invoice_id, product_id, ))
        self.conn.commit()

    def plus_quantity(self, invoice_id, product_id):
        update_statement = """
            UPDATE invoices
            SET quantity = quantity + 1
            WHERE invoice_id = %s AND product_id = %s
            """
        self.cursor.execute(update_statement, (invoice_id, product_id, ))
        self.conn.commit()
    def delete_invoice(self, invoice_id):
        delete_statement = """
        DELETE FROM `invoices` WHERE invoice_id = %s
        """
        self.cursor.execute(delete_statement, (invoice_id, ))
        self.conn.commit()

    def delete_product(self, product_id):
        delete_statement = """
        DELETE FROM `product` WHERE id = %s
        """
        self.cursor.execute(delete_statement, (product_id, ))
        self.conn.commit()

    def increase_user_invoice_id(self, user_id):
        update_statement = """
        UPDATE users
        SET num_sales = num_sales + 1
        WHERE id = %s
        """
        self.cursor.execute(update_statement, (user_id, ))
        self.conn.commit()

    def add_sales(self, invoice_id, total, date):
        insert_statement = """
            INSERT INTO sales 
            (invoice_id, amount, date)
            VALUES (%s, %s, %s);
            """
        self.cursor.execute(insert_statement, (invoice_id, total, date, ))
        self.conn.commit()

    def update_product(self, id, name, price, category, description, path):
        update_statement = """
        UPDATE product
        SET name = %s, price = %s, kategori = %s, Deskripsi = %s, path = %s
        WHERE product.id = %s
        """
        self.cursor.execute(update_statement, (name, price, category, description, path, id,))
        self.conn.commit()

    def add_product(self, name, price, category, description, path):
        insert_statement = f"INSERT INTO product (name, price, kategori, Deskripsi, path) VALUES ('{name}', '{price}', '{category}' ,'{description}', '{path}')"
        self.cursor.execute(insert_statement)
        self.conn.commit()
    
    def get_invoices_by_id(self, sales_id):
        select_statement = """
        SELECT `sales`.`date`,  `invoices`.`invoice_id`, `product`.`name`, `invoices`.`quantity` , `product`.`price` 
        FROM `sales`
        INNER JOIN `invoices` on `invoices`.`invoice_id` = `sales`.`invoice_id`
        INNER JOIN `product` on `invoices`.`product_id` = `product`.`id`
        WHERE `sales`.`sales_id` = %s
        """
        self.cursor.execute(select_statement, (sales_id, ))
        sales = self.cursor.fetchall()
        return sales

    def get_sales(self):
        select_statement = """
        SELECT * FROM sales
        """
        self.cursor.execute(select_statement)
        sales = self.cursor.fetchall()
        return sales

    def search_product(self, keyword):
        select_statement = f"SELECT * FROM product WHERE `product`.`name` LIKE '%{keyword}%'"
        self.cursor.execute(select_statement)
        all_products = self.cursor.fetchall()
        return all_products #(id, name, price, kategori, deskripsi, path)

    def get_user_email_by_username(self, username):
        select_statement = """
        SELECT email FROM users
        WHERE username = %s
        """
        self.cursor.execute(select_statement, (username,))
        email = self.cursor.fetchall()
        return email

    def get_all_user_email(self):
        select_statement = """
        SELECT email FROM users
        """
        self.cursor.execute(select_statement)
        emails = self.cursor.fetchall()
        return emails

    def get_sales_by_date(self, start_date, end_date):
        select_statement = """
        SELECT * FROM sales
        WHERE (date >= %s) AND (date <= %s)
        """
        self.cursor.execute(select_statement, (start_date, end_date,))
        sales = self.cursor.fetchall()
        return sales