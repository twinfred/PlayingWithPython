name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def create_dict(x,y):
    my_dict = {}
    for i in range(0, len(x)):
        my_dict[x[i]] = y[i]
    return my_dict

output = create_dict(name,favorite_animal)

print output