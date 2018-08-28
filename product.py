class Product(object):
    def __init__(self,price,item_name,weight,brand):
        self.price = round(price,2)
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
        self.display_info()
    
    def sell(self):
        self.status = 'sold'
        return self
    
    def addTax(self,tax):
        self.price = round(self.price * (1+tax),2)
        return self
    
    def return_item(self,reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        if reason == 'changed mind, box like new':
            self.status = 'for sale'
        if reason == 'open box':
            self.status = 'used'
            self.price *= 0.80 
        return self

    def display_info(self):
        print 'Item Name: '+str(self.item_name)
        print 'Price: $'+str(self.price)
        print 'Weight: '+str(self.weight)+'lbs' 
        print 'Brand: '+str(self.brand)
        print 'Item Status: '+str(self.status)

product1 = Product(56.70, 'webcam', 5.7, 'Logitech')
# product1.display_info()
# product1.addTax(.15).sell()
# product1.display_info()
# product1.return_item('defective').display_info()
# product1.return_item('changed mind, box like new').display_info()
# product1.return_item('open box').display_info()

    

