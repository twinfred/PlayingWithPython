class Product(object):
    def __init__(self,price,item_name,weight,brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
        self.tax = 0
        self.display_info()
    def item_sold(self):
        self.status = "Sold"
        return self
    def plus_tax(self):
        self.tax = self.price * 0.0975
        self.price += self.tax
        return self
    def item_returned(self,condition):
        if(condition == "Defective"):
            self.status = "Defective"
            self.price = 0
            self.tax = 0
        elif(condition == "Like New"):
            self.status = "For Sale"
            self.tax = 0
        elif(condition == "Opened"):
            self.status = "For Sale"
            self.price = (self.price - (self.price * 0.2)) - self.tax
            self.tax = 0
        return self
    def display_info(self):
        print "ITEM INFO"
        print "Price: $" + str(self.price)
        print "Name: " + str(self.item_name)
        print "Weight: " + str(self.weight) + "lbs"
        print "Brand: " + str(self.brand)
        print "Status: " + str(self.status)
        print "Sales Tax: $" + str(self.tax)
        return self

item1 = Product(14.99,"Water Bottle",1.5,"REI")
item1.plus_tax().display_info().item_sold().display_info().item_returned("Opened").display_info()