from flask import Flask, render_template, session, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

def initialize_global_data():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Password",
        database="products"
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM inventory;")
    rows = cursor.fetchall()
    cursor.close()
    mydb.close()

    products_data = []
    for row in rows:
        product_dict = {
            "id": row[0],
            "name": row[1],
            "type": row[2],
            "price": row[3],
            "image_path": row[4]
        }
        products_data.append(product_dict)

    return products_data

@app.route('/', methods=['GET'])
def get_products():
    # Initialize cart in session if not present
    if 'cart' not in session:
        session['cart'] = []

    # Initialize global product data within the context of a request
    global global_products_data
    global_products_data = initialize_global_data()

    return render_template('index.html', products=global_products_data)

@app.route('/breads', methods=['GET'])
def get_breads():
    return render_template('breads.html', products=global_products_data)

@app.route('/drinks', methods=['GET'])
def get_drinks():
    return render_template('drinks.html', products=global_products_data)

@app.route('/fruits', methods=['GET'])
def get_fruits():
    return render_template('fruits.html', products=global_products_data)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = next((p for p in global_products_data if p['id'] == product_id), None)

    if product:
        existing_item = next((item for item in session['cart'] if item['id'] == product_id), None)

        if existing_item:
            existing_item['quantity'] += 1
        else:
            session['cart'].append({
                'id': product['id'],
                'name': product['name'],
                'price': product['price'],
                'quantity': 1
            })

    return redirect(request.referrer or url_for('get_products'))

@app.route('/view_cart', methods=['GET'])
def view_cart():
    return render_template('cart.html', cart=session['cart'])

@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    product = next((p for p in global_products_data if p['id'] == product_id), None)

    if product:
        for item in session['cart']:
            if item['id'] == product_id:
                session['cart'].remove(item)
                break

    return redirect(url_for('view_cart'))

def count_items(cart):
    return len(cart) if cart else 0

# Add the filter to the Jinja2 environment
app.jinja_env.filters['count_items'] = count_items
def get_total_price():
    # Calculate the total price of items in the cart
    total_price = sum(item['price'] for item in session['cart'])
    return f"${total_price:.2f}"

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    print("Cart:", session['cart'])
    user_details = session.get('user_details', 'Guest')
    return render_template('checkout.html', user_details=user_details, cart=session['cart'], total_price=get_total_price(), count_items=count_items)
@app.route('/process_checkout', methods=['POST'])
def process_checkout():
    # Retrieve form data from the checkout form
    billing_address = {
        'full_name': request.form.get('firstname'),
        'email': request.form.get('email'),
        'address': request.form.get('address'),
        'city': request.form.get('city'),
        'zip': request.form.get('zip'),
    }

    # Store the billing address and payment information in the database
    store_checkout_data(billing_address)

    # Clear the cart after placing the order
    session['cart'] = []

    return redirect(url_for('thank_you'))



def store_checkout_data(billing_address):
    # Store the checkout data in the database (Modify as needed)
    # For simplicity, I'm assuming you have a table named 'checkout_data'
    # with columns: id, full_name, email, address, city, state, zip,
    # card_name, card_number, exp_month, exp_year, cvv
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Samsungnote10+",
        database="products"  # Replace with your actual database name
    )
    cursor = mydb.cursor()

    cursor.execute("""
        INSERT INTO checkout_data
        (full_name, email, address, city, zip)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        billing_address['full_name'], billing_address['email'], billing_address['address'],
        billing_address['city'], billing_address['zip']
    ))

    mydb.commit()
    cursor.close()
    mydb.close()

@app.route('/thank_you', methods=['GET'])
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
