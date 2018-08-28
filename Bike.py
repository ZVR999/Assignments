# Added if statement to reverse() to stop miles from becoming negative
# Return self should be added to any method that changes an object

class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    
    def displayInfo(self):
        print self.price, self.max_speed, self.miles

    def ride(self):
        print 'Riding'
        self.miles += 10
        return self
    
    def reverse(self):
        print 'Reversing'
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self

bike1 = Bike(3000, 100, 0)
bike2 = Bike(3000, 100, 0)
bike3 = Bike(3000, 100, 0)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()



# python random.py