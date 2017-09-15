class Product(object):
    def __init__(self, price, item, weight, brand, cost, status = 'for sale'):
        self.price = price
        self.item = item
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'for sale'
    def sell(self):
        self.status = 'sold'
        return self
    def tax(self, tax):
        total = self.price * (1 + tax)
        return total
    def returnItem(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'in the box, like new':
            self.status = 'for sale'
        elif reason == 'opened':
            self.status = 'used'
            self.price *= 0.80
        return self
    def displayInfo(self):
        print 'Price: $' + str(self.price) + '\nItem: ' + self.item + '\nWeight: ' + str(self.weight) + 'lbs\nBrand: ' + self.brand + '\nCost: ' + str(self.cost) + '\nStatus: ' + self.status
        return self
phone = Product(500, 'iPhone', 2, 'Apple', 200)
phone.displayInfo().sell().displayInfo().returnItem('defective').displayInfo()
