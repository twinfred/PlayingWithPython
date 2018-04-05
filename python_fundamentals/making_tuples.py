my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dict_in_tuples_out(x):
    tuples_list = []
    for key,value in x.iteritems():
        y = (key,value)
        tuples_list.append(y)
    return tuples_list

output = dict_in_tuples_out(my_dict)

print output