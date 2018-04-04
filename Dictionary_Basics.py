tim_dict = {
    "name" : "Tim",
    "age" : 28,
    "height" : "5 foot 7 inches",
    "eye color" : "hazel",
    "city of birth" : "Martinez"
}

def who_is(x):
    for key,value in x.iteritems():
        print "My " + str(key) + " is " + str(value) + "."

who_is(tim_dict)