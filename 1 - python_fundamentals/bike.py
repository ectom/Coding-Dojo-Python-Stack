class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "Price: $" + str(self.price) + ', Max Speed: ' + str(self.max_speed) + 'mph, Miles: ' + str(self.miles)
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        if self.miles < 5:
            print "Cannot Reverse"
            self.displayInfo()
            exit()
        print "Reversing"
        self.miles -= 5
        return self
bike = Bike(100, 50, 0)
bike.ride().reverse().reverse().reverse().displayInfo()
