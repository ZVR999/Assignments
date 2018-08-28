class Store(object):
    def __init__(self,products,location,owner):
        self.products = products
        self.location = location
        self.owner = owner
    
    def add_product(self,product):
        products = self.products
        products.append(product)  
        return self
    
    def remove_product(self,product_name):
        products = self.products
        for product in products:
            if product.name == product_name:
                products.remove(product)
        
        return self

    def inventory(self):
        products = self.products
        for product in products:
            print 'Product Name: '+product.name
            print 'Product Category: '+product.category

    def display_store(self):
        products = self.products
        pro = 'Products: '
        for product in products:
            pro += str(product.name)
        print pro
        print 'Location: '+str(self.location)
        print 'Owner: '+str(self.owner)

class Product(object):
    def __init__(self,name,category):
        self.name = name
        self.category = category
    
    def display_info(self):
        print self.category

product1 = Product('tooth brush','hygine')
product2 = Product('hair brush','grooming')
# product1.display_info()
store1 = Store([],'moon','Star Fox')
# store1.display_store()
store1.add_product(product1).add_product(product2).display_store()
# store1.inventory()
store1.remove_product('hair brush').display_store()
