def type_list(my_list):
    # Setting variables
    new_string = 'String: '
    int_sum = 0
    string_count = 0
    int_count = 0
    
    # Checking type of the list indexes
    for i in range(0, len(my_list)):
        # Checking list for strings
        if isinstance(my_list[i], str):
            new_string += my_list[i] + " "
            string_count += 1
        # Checking list for numbers
        elif isinstance(my_list[i], int):
            int_sum += my_list[i]
            int_count += 1
    
    # Check list type
    if string_count > 0 and int_count > 0:
        print "The list you entered is of mixed type."
        print new_string
        print int_sum
    elif string_count > 0 and int_count == 0:
        print "The list you entered is of string type"
        print new_string
    elif string_count == 0 and int_count > 0:
        print "The list you entered is of integer type"
        print int_sum
    
type_list([0, 1, 5, "Tim", "was", "here"])