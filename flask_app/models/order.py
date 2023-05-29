
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Order:
    db = "cookies_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Orders Models
    @classmethod
    def save_order(cls, data):
        query = """
        INSERT INTO orders (name, cookie_type, num_of_boxes)
        VALUES (%(name)s, %(cookie_type)s, %(num_of_boxes)s)
        ; """

        return connectToMySQL(cls.db).query_db(query, data)



    # Read Orders Models
    @classmethod
    def get_all_orders(cls):
        query = """ SELECT * FROM orders;
        """
        orders_data = connectToMySQL(cls.db).query_db(query)
        orders = []
        for order in orders_data:
            orders.append(cls(order))

        return orders

    @classmethod
    def get_one_order(cls, order_id):
        query = """ SELECT * FROM orders
        WHERE id = %(id)s
        ; """
        orders_data = connectToMySQL(cls.db).query_db(query, {'id': order_id})
        return cls(orders_data[0])

    # Update Orders Models
    @classmethod
    def update_order(cls, data):
        query = """ UPDATE orders
        SET name=%(name)s, cookie_type=%(cookie_type)s, num_of_boxes=%(num_of_boxes)s
        WHERE id = %(id)s
        ; """
        return connectToMySQL(cls.db).query_db(query, data)



    # Delete Orders Models

    #Validations
    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order['name']) < 2:
            is_valid = False
            flash("Error: To get cookies your name must be at least 2 characters long!")
        if int(order['num_of_boxes']) > 100 or int(order['num_of_boxes']) < 1:
            is_valid = False
            flash("Error: Orders must be between 1-100 boxes")
        return is_valid