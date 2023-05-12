from flask import Flask, render_template, request

app = Flask(__name__)
products = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    price = request.form['price']
    products.append({'name': name, 'price': int(price)})
    return render_template('index.html', products=products)

@app.route('/update', methods=['POST'])
def update_product():
    name = request.form['name']
    new_price = request.form['new_price']
    for product in products:
        if product['name'] == name:
            product['price'] = new_price
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)