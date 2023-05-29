from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import order # import entire file, rather than class, to avoid circular imports

# Create Users Controller
@app.route('/cookies/new')
def order_form():
    return render_template('order.html')

@app.route('/cookies/new/order', methods=['POST'])
def save_order():
    if not order.Order.validate_order(request.form):
        return redirect('/cookies/new')
    order.Order.save_order(request.form)
    return redirect('/cookies')


# Read Users Controller

@app.route('/')
def root():    
    return redirect('/cookies')

@app.route('/cookies')
def cookie_orders():
    return render_template('cookies.html', orders = order.Order.get_all_orders())



# Update Users Controller
@app.route('/order/<int:order_id>')
def update_order(order_id):
    return render_template('update_order.html', one_order = order.Order.get_one_order(order_id))

@app.route('/cookies/update/order', methods=['POST'])
def update_order_process():
    if not order.Order.validate_order(request.form):
        return redirect(f"/order/{request.form['id']}")
    order.Order.update_order(request.form)
    return redirect('/cookies')


# Delete Users Controller


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')
# def index(id):
#     user_info = user.User.get_user_by_id(id)
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.