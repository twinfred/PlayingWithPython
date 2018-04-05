word = "It's thanksgiving day. It's my birthday,too!"
print word.find('day')
print word.replace('day', 'month')

y = [2, 54, -2, 7, 12, 98]
print min(y)
print max(y)

x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0], x[len(x)-1]
new_x = [x[0], (x[len(x)-1])]
print new_x

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
z_first = z[:5]
z_second = z[5:]
z_output = [z_first, z[5], z[6], z[7], z[8], z[9]]
print z_output