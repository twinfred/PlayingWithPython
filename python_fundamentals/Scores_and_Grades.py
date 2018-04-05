def scores_grades():
    print "Scores and Grades"
    for x in range(0,10):
        import random
        random_num = random.randint(60,100)
        if random_num >= 90:
            print "Score: " + str(random_num) + "; Your grade is A."
        elif random_num >= 80:
            print "Score: " + str(random_num) + "; Your grade is B."
        elif random_num >= 70:
            print "Score: " + str(random_num) + "; Your grade is C."
        elif random_num >= 60:
            print "Score: " + str(random_num) + "; Your grade is D."
    print "End of the program. Bye!"
scores_grades()