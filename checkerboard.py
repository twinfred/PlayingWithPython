line = 0
for i in range(0,4):
    print "* * * * \n * * * *"
# ALT OPTION
row = 0
for i in range(0,4):
    if row == 0:
        print "* * * * "
        row = 1
    else:
        print " * * * *"
        row = 0