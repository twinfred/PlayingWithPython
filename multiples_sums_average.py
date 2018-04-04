# Multiples - Part 1
for i in range(1, 1001, 2):
    print i

# Multiples - Part 2
for i in range(5, 1000000, 5):
    print i

# Sum List
x = [1, 2, 5, 10, 255, 3]
def sum_list(my_arr):
    arr_sum = 0
    for i in range(0, len(my_arr)):
        arr_sum += my_arr[i]
    print arr_sum
sum_list(x)

# Average List
x = [1, 2, 5, 10, 255, 3]
def avg_list(y):
    y_sum = 0
    for i in range(0, len(y)):
        y_sum += y[i]
    avg = y_sum / len(y)
    print avg
avg_list(x)