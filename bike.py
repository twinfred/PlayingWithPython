class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def display_info(self):
        print "This bike costs $" + str(self.price) + " dollars, has a max speed of " + str(self.max_speed) + " MPH, and has been riden " + str(self.miles) + " miles."
    def ride(self):
        print "Riding bike."
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing bike."
        self.miles -= 5
        if(self.miles < 0):
            self.miles = 0
        return self

bike1 = Bike(200,50)
bike1.ride().ride().ride().reverse().display_info()

bike2 = Bike(500,100)
bike2.ride().ride().reverse().reverse().display_info()

bike3 = Bike(100, 30)
bike3.reverse().reverse().reverse().display_info()