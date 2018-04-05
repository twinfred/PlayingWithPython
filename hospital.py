class Patient(object):
    def __init__(self, patient_id, name, allergies):
        self.patient_id = patient_id
        self.name = name
        self.allergies = allergies
        self.bed_number = None

class Hospital(object):
    def __init__(self):
        self.name = "Burbank General Hospital"
        self.max_capacity = 10
        self.patients = []
        self.avail_beds = [1,2,3,4,5,6,7,8,9,10]
    def admit(self, patient_id, name, allergies):
        if len(self.patients) >= self.max_capacity:
            print "A new patient wants to be admitted..."
            print "Available Beds:",str(self.avail_beds)
            print "Patient not admitted. Hospital is full."
            return self
        else:
            self.new_patient = Patient(patient_id, name, allergies)
            self.patients.append(self.new_patient)
            print "A new patient wants to be admitted..."
            print "Available Beds:",str(self.avail_beds)
            self.new_patient.bed_number = self.avail_beds[0]
            for x in range (1, len(self.avail_beds)):
                self.avail_beds[x-1] = self.avail_beds[x]
            self.avail_beds.pop()
            print "Patient was admitted to bed number:",str(self.new_patient.bed_number)+"."
            print "Patient Name:", str(self.new_patient.name)+"."
            return self
    def discharge(self, patient_id):
        self.being_discharged = ""
        self.updated_patients = []
        for x in range (0, len(self.patients)):
            if (patient_id - 1) == x:
                print "Patient being dischraged:", str(self.patients[x].name)+". Patient was in bed number:", self.patients[x].bed_number
                self.avail_beds.append(self.patients[x].bed_number)
                self.being_discharged = x
        for x in range (0, len(self.patients)):
            if x == self.being_discharged:
                continue
            else:
                self.updated_patients.append(x)
        self.patients = self.updated_patients


hospital = Hospital()

add_patient1 = hospital.admit(1, "Tim", "sulfa")
add_patient2 = hospital.admit(2, "Jason", "bees")

print "\nCurrent Hospital Patient Count...", str(len(hospital.patients))+"\n "

dischrage_patient1 = hospital.discharge(2)

print "\nCurrent Hospital Patient Count...", str(len(hospital.patients))+"\n "

add_patient3 = hospital.admit(3, "Max", "nuts")
add_patient4 = hospital.admit(4, "Justin", "sulfa")
add_patient5 = hospital.admit(5, "Hector", "bees")
add_patient6 = hospital.admit(6, "Alex", "sulfa")

dischrage_patient1 = hospital.discharge(5)

print "\nCurrent Hospital Patient Count...", str(len(hospital.patients))+"\n "

add_patient7 = hospital.admit(7, "Tom", "bees")
add_patient8 = hospital.admit(8, "Peter", "sulfa")
add_patient9 = hospital.admit(9, "Apple", "bees")
add_patient10 = hospital.admit(10, "Banana", "sulfa")
add_patient11 = hospital.admit(11, "Sam", "bees")
add_patient12 = hospital.admit(12, "Katie", "sulfa")
add_patient13 = hospital.admit(13, "Laurie", "bees")

print "\nCurrent Hospital Patient Count...", str(len(hospital.patients))+"\n "

dischrage_patient1 = hospital.discharge(9)

print "\nCurrent Hospital Patient Count...", str(len(hospital.patients))+"\n "

add_patient7 = hospital.admit(14, "Hank", "bees")
add_patient8 = hospital.admit(15, "Greg", "sulfa")
add_patient9 = hospital.admit(16, "Roger", "bees")