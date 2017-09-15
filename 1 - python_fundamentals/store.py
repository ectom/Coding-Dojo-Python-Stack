class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    def add_product(self, product):
        self.products.append(product)
        return self
    def remove_product(self, product):
        self.products.remove(product)
        return self
    def inventory(self):
        print self.products
        return self
stuff = Store(['car', 'charger', 'bottle'], 'San Francisco', 'John Smith')
stuff.add_product('water').remove_product('car').inventory()
