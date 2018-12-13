class Person:
    def __init__(self):
        self.name = "Arif"
        self.dob = self.DOB()
    def display(self):
        print("Person Name: {}".format(self.name))
        self.dob.display()
    class DOB:
        def __init__(self):
            self.dd = 25
            self.mm = 1
            self.yyyy = 1990
        def display(self):
            print("DOB = {}/{}/{}".format(self.dd,self.mm, self.yyyy))

p = Person()
p.display()