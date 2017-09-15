class Patient(object):
    def __init__(self, idNum, name, allergy, bed = None):
        self.idNum = idNum
        self.name = name
        self.allergy = allergy
        self.bed = bed
    def display(self):
        print str(self.idNum) + ' ' + self.name + ' ' + self.allergy + ' ' + str(self.bed)
        return self
class Hospital(Patient):
    def __init__(self, hName, capacity):
        self.patients = []
        self.hName = hName
        self.capacity = capacity
    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "The hospital is full. Come back later"
        else:
            self.patients.append(patient)
            self.bed = 1
            print "Patient admitted"
            for i in self.patients:
                i.display()
        return self
    def remove(self, name):
        self.bed = None
        for i in range(len(self.patients)-1):
            if self.name[i] == name:
                self.patients.pop(i)
                for k in self.patients:
                    k.display()
        return self
guy = Patient(167890, 'guy', 'clams')
hospital = Hospital('Kaiser', 100)
hospital.admit(guy).remove(guy)
