import shelve, secrets

# Product Class


class Product:
    def __init__(self, id, name, sku, quantity, price, status, discount, category, image=None):
        self.__id = id
        self.__name = name
        self.__sku = sku
        self.__quantity = quantity
        self.__price = price
        self.__status = status
        self.__discount = discount
        self.__category = category
        self.__image = image

    def get_product_id(self):
        return self.__id

    def get_product_name(self):
        return self.__name

    def get_product_sku(self):
        return self.__sku

    def get_product_quantity(self):
        return self.__quantity

    def get_product_price(self):
        return self.__price

    def get_product_status(self):
        return self.__status

    def get_product_discount(self):
        return self.__discount

    def get_product_category(self):
        return self.__category

    def get_product_image(self):
        return self.__image

    def set_product_id(self, id):
        self.__id = id

    def set_product_name(self, name):
        self.__name = name

    def set_product_sku(self, sku):
        self.__sku = sku

    def set_product_quantity(self, quantity):
        self.__quantity = quantity

    def set_product_price(self, price):
        self.__price = price

    def set_product_status(self, status):
        self.__status = status

    def set_product_discount(self, discount):
        self.__discount = discount

    def set_product_category(self, category):
        self.__category = category

    def set_product_image(self, image):
        self.__image = image


class ProductsManagement:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def view_product(self):
        with shelve.open(self.db_path) as db:
            for product_id_str, product_instance in db.items():
                try:
                    # Try to convert the key to an integer
                    # product_id = int(product_id_str)
                    pass
                except ValueError:
                    # Skip this entry if the key is not a valid integer
                    # print(f"Skipping invalid key: {product_id_str}")
                    continue

                # Now you can access the methods of the Product instance
                print(f"id: {product_id_str}, name: {product_instance.get_product_name()}, "
                      f"sku: {product_instance.get_product_sku()}, quantity: {product_instance.get_product_quantity()}, "
                      f"price: {product_instance.get_product_price()}, status: {product_instance.get_product_status()}, "
                      f"discount: {product_instance.get_product_discount()}, category: {product_instance.get_product_category()}")
            return True

    def create_product(self, product):
        with shelve.open(self.db_path, writeback=True) as db:
            product_id = product.get_product_id()
            if product_id in db:
                print("Product with ID already exists.")
                return False
            db[product_id] = product
            print("Product created without problem.")

            db.close()
        return True

    def delete_product(self, product_id):
        with shelve.open(self.db_path) as db:
            if product_id in db:
                del db[product_id]
                return True
        return False

    def filter_products_by_category(self, category):
        with shelve.open(self.db_path) as db:
            filtered_products = [
                product for product in db.values() if product.get_product_category().lower() == category.lower()]
        return filtered_products


