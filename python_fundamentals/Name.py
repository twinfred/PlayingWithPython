# Part 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_names(names_dict):
    for x in range(0, len(names_dict)):
        print names_dict[x]["first_name"], names_dict[x]["last_name"]

print_names(students)

# Part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def students_intructors(school_roster):
    # Print Student Info
    print "Students"
    for x in range(0,len(school_roster["Students"])):
        student_id = x + 1
        first_name = school_roster["Students"][x]['first_name']
        last_name = school_roster["Students"][x]['last_name']
        name_char_length = len(first_name) + len(last_name)
        print str(student_id) + " - " + first_name, last_name + " - " + str(name_char_length)
    #Print Instructor Info
    print "Instructors"
    for x in range(0,len(school_roster["Instructors"])):
        instructor_id = x + 1
        first_name = school_roster["Instructors"][x]['first_name']
        last_name = school_roster["Instructors"][x]['last_name']
        name_char_length = len(first_name) + len(last_name)
        print str(instructor_id) + " - " + first_name, last_name + " - " + str(name_char_length)

students_intructors(users)