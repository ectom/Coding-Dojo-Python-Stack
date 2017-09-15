class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def displayAll(self):
        print "Price: " + str(self.price) + '\nSpeed: ' + str(self.speed) + 'mph\nFuel: ' + self.fuel + '\nMileage: ' + str(self.mileage) + 'mpg\nTax: ' + str(self.tax)
car = Car(20000, 70, 'Full', 40)
car.displayAll()
