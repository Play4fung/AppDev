from flask import Flask, render_template, request, redirect, url_for
import os
import shelve
import secrets
from werkzeug.utils import secure_filename
from Classes import Product

app = Flask(__name__)

productDict = {}
db = shelve.open('products.db', 'c')
try:
    if 'Products' in db:
        productDict = db['Products']
    else:
        db['Products'] = productDict
except:
    print("Error in opening products.db.")


# Set the path where uploaded images will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def get_next_id():
    existing_ids = set(productDict.keys())

    while True:
        product_id = secrets.token_hex(8)[:8]

        if product_id not in existing_ids:
            return product_id


@app.route('/')
def home():
    return render_template('index.html', products=productDict)


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        try:
            id = get_next_id()
            name = request.form['name']
            sku = request.form['sku']
            quantity = int(request.form['quantity'])
            price = float(request.form['price'])
            status = request.form['status']
            discount = float(request.form['discount'])
            detail = request.form['detail']

            # Handle image file upload
            thumbnail = request.files['thumbnail']
            if thumbnail:
                filename1 = secure_filename(thumbnail.filename)
                filepath1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
                thumbnail.save(filepath1)
            else:
                filepath1 = None

            # Handle image file upload
            images = request.files['images']
            if images:
                filename2 = secure_filename(images.filename)
                filepath2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
                images.save(filepath2)
            else:
                filepath2 = None

            # Handle image file upload
            more_detailed_images = request.files['more_detailed_images']
            if images:
                filename3 = secure_filename(more_detailed_images.filename)
                filepath3 = os.path.join(app.config['UPLOAD_FOLDER'], filename3)
                more_detailed_images.save(filepath3)
            else:
                filepath3 = None

            type = request.form['type']

            product = Product(id=id, name=name, sku=sku, quantity=quantity, price=price, status=status, discount=discount, detail=detail, thumbnail=filepath1, images=filepath2, more_detailed_images=filepath3, type=type)
            productDict[product.get_product_id()] = product

            # Update the orders database
            with shelve.open("products.db") as db:
                db['Products'] = productDict
                db.close()
            return redirect(url_for('home'))

        except Exception as e:
            print("Error adding product:", str(e))

    return render_template('add_product.html')


@app.route('/delete_product/<product_id>')
def delete_product(product_id):
    productDict.pop(product_id, None)
    db['Products'] = productDict
    return redirect(url_for('home'))


@app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = productDict.get(product_id)

    if not product:
        return redirect(url_for('home'))

    if request.method == 'POST':
        name = request.form['name']
        sku = request.form['sku']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        status = request.form['status']
        discount = float(request.form['discount'])
        category = request.form['category']

        # Update the product information
        product.set_product_name(name)
        product.set_product_sku(sku)
        product.set_product_quantity(quantity)
        product.set_product_price(price)
        product.set_product_status(status)
        product.set_product_discount(discount)
        product.set_product_category(category)

        with shelve.open("products.db") as db:
            db['Products'] = productDict
            db.close()
        return redirect(url_for('home'))

    return render_template('edit_product.html', product=product)


@app.route('/filter_products', methods=['POST'])
def filter_products():
    selected_categories = request.form.getlist('selected_categories[]')

    if 'all' in selected_categories:
        filtered_products = productDict
    else:
        filtered_products = {
            product_id: product
            for product_id, product in productDict.items()
            if product.get_product_type().lower() in map(str.lower, selected_categories)
        }

    return render_template('index.html', products=filtered_products)


if __name__ == '__main__':
    app.run()
