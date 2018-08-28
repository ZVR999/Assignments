class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price < 10000:
            self.tax = 0.12
        else:
            self.tax = 0.15
    
    def display_all(self):
        print 'Price:'+str(self.price)
        print 'Speed:'+str(self.speed)
        print 'Fuel:'+str(self.fuel)
        print 'Mileage'+str(self.mileage)
        print 'Tax:'+str(self.tax)
        print '*'* 50
 
car1 = Car(2500, 35, 'Full', 15).display_all()
car2 = Car(7591, 5, 'Not Full', 105).display_all()
car3 = Car(10000, 15, 'Kind of Full', 95).display_all()
car4 = Car(2000, 25, 'Full', 25).display_all()
car5 = Car(25000, 45, 'Full', 85).display_all()
car6 = Car(1170, 45, 'Empty', 15).display_all()

# print car1.display_all(), car2.display_all(), car3.display_all(), car4.display_all(), car5.display_all(), car6.display_all()



    
    

