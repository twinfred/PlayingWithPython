def odd_even():
    for i in range(1,2001):
        if i % 2 == 0:
            print "Number is " + str(i) + ". This is an even number."
        if i % 2 != 0:
            print "Number is " + str(i) + ". This is an odd number."
odd_even()

def multiply(my_list, mult):
    new_list = []
    for x in my_list:
        x *= mult
        new_list.append(x)
    print new_list
multiply([5,10,20,1], 5)