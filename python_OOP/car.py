class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if(price < 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    def display_all(self):
        print "Price:", str(self.price)
        print "Speed:", str(self.speed), "mph"
        print "Fuel:", str(self.fuel)
        print "Mileage:", str(self.mileage), "mpg"
        print "Tax:", str(self.tax)

car1 = Car(5000,40,"Full",35)
car2 = Car(12000,80,"Half Full",45)
car3 = Car(2000,15,"Nearly Empty",20)
car4 = Car(4000,35,"Full",30)
car5 = Car(20000,150,"Super Full",90)
car6 = Car(500,5,"Empty",5)