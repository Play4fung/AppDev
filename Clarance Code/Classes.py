import shelve, secrets

class Product:
    def __init__(
        self,
        id,
        name,
        sku,
        quantity,
        price,
        status,
        discount,
        detail,
        thumbnail,
        images,
        more_detailed_images,
        type,
    ):
        self.__id = id
        self.__name = name
        self.__sku = sku
        self.__quantity = quantity
        self.__price = price
        self.__status = status
        self.__discount = discount
        self.__detail = detail
        self.__thumbnail = thumbnail
        self.__images = images
        self.__more_detailed_images = more_detailed_images
        self.__type = type
        self.__reviews = []

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

    def get_product_detail(self):
        return self.__detail

    def get_product_thumbnail(self):
        return self.__thumbnail

    def get_product_images(self):
        return self.__images

    def get_product_more_detailed_images(self):
        return self.__more_detailed_images

    def get_product_type(self):
        return self.__type

    def get_reviews(self):
        return self.__reviews

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

    def set_product_detail(self, detail):
        self.__detail = detail

    def set_product_thumbnail(self, thumbnail):
        self.__thumbnail = thumbnail

    def set_product_images(self, images):
        self.__images = images

    def set_product_more_detailed_images(self, more_detailed_images):
        self.__more_detailed_images = more_detailed_images

    def set_product_type(self, type):
        self.__type = type

    def set_reviews(self, reviews):
        self.__reviews = reviews

    def add_review(self, user, rating, comment):
        review = {"user": user, "rating": rating, "comment": comment}
        self.__reviews.append(review)

    def __str__(self):
        return f"Name: {self.__name}\nDetail: {self.__detail}\nPrice: {self.__price}\nType: {self.__type}"


class Keyboard(Product):
    def __init__(
        self,
        id,
        name,
        sku,
        quantity,
        price,
        status,
        discount,
        detail,
        thumbnail,
        images,
        more_detailed_images,
        switch,
    ):
        super().__init__(
            id,
            name,
            sku,
            quantity,
            price,
            status,
            discount,
            detail,
            thumbnail,
            images,
            more_detailed_images,
            type="keyboard",
        )
        self.__switch = switch

    def get_switch(self):
        return self.__switch

    def set_switch(self, switch):
        self.__switch = switch


class KeyCaps(Product):
    def __init__(
        self,
        id,
        name,
        sku,
        quantity,
        price,
        status,
        discount,
        detail,
        thumbnail,
        images,
        more_detailed_images,
        type="keycaps",
    ):
        super().__init__(
            id,
            name,
            sku,
            quantity,
            price,
            status,
            discount,
            detail,
            thumbnail,
            images,
            more_detailed_images,
            type,
        )


class Switches(Product):
    def __init__(
        self,
        id,
        name,
        sku,
        quantity,
        price,
        status,
        discount,
        detail,
        thumbnail,
        images,
        more_detailed_images,
        type="switches",
    ):
        super().__init__(
            id,
            name,
            sku,
            quantity,
            price,
            status,
            discount,
            detail,
            thumbnail,
            images,
            more_detailed_images,
            type,
        )


class Accessories(Product):
    def __init__(
        self,
        id,
        name,
        sku,
        quantity,
        price,
        status,
        discount,
        detail,
        thumbnail,
        images,
        more_detailed_images,
        type="accessories",
    ):
        super().__init__(
            id,
            name,
            sku,
            quantity,
            price,
            status,
            discount,
            detail,
            thumbnail,
            images,
            more_detailed_images,
            type,
        )
