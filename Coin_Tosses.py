def coin_flip_5000 ():
    print "Starting the program..."
    # Keeping Track of Flip Results
    head_count = 0
    tail_count = 0
    # Flip Coin 5000 times
    for x in range (1,5001):
        # Generate Random Number (Heads = 0, Tails = 1)
        import random
        coin_flip = random.randint(0,1)
        # If Heads...
        if coin_flip == 0:
            head_count += 1
            print "Attempt #" + str(x) + ": Throwing a coint... It's a head! ... Got " + str(head_count) + " heads(s) so far and " + str(tail_count) + " tail(s) so far."
        # If Tails...
        if coin_flip == 1:
            tail_count += 1
            print "Attempt #" + str(x) + ": Throwing a coint... It's a tail! ... Got " + str(head_count) + " heads(s) so far and " + str(tail_count) + " tail(s) so far."
    print "Ending the program, thank you!"
    

coin_flip_5000()