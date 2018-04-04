x = 1000
y = "Welcome to Coding Dojo!"
z = [1,2,3,4,5,6,7,8,9,10,11]

def filter_by_type(filter_value):
    # For: INTEGERS
    if isinstance(filter_value, int):
        if filter_value >= 100:
            print "That's a big number!"
        else:
            print "That's a small number."
    # For: STRINGS
    elif isinstance(filter_value, str):
        if len(filter_value) >= 50:
            print "Long sentence."
        else:
            print "Short sentence."
    # For: LIST
    elif isinstance(filter_value, list):
        if len(filter_value) >= 10:
            print "Big list!"
        else:
            print "Short list."
            
filter_by_type(x)
filter_by_type(y)
filter_by_type(z)