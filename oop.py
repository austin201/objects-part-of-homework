import datetime
import time
class person(object):
    def __init__(self,name,last,age,haircolor,eyecolor,weight):
        self.bday = datetime.datetime.now().time()
        self.lastbday = self.bday
        self.height = 0
        self.wingspan = ""
        self.weight = weight
        self.haircolor = haircolor
        self.eyecolor = eyecolor
        self.hairlength = ""
        self.vision = 0
        self.age = age
        self.necklength = ""
        self.gender = ""
        self.iq = 0
        self.limbs = ""
        self.firstName = name
        self.lastName = last
    def intro(self):
        print("hello My name is "+self.firstName + " "+self.lastName +"\nI have "+self.haircolor +" hair and "+self.eyecolor+" eyes and I am "+str(self.age) +" years old\nand I am "+str(self.weight)+" pounds")
    def aging(self):
        ctime = datetime.datetime.now().time()
        delta = datetime.timedelta(minutes=1)
        checktime = self.lastbday + delta
        if ctime >= checktime:
            self.age += 1
            self.lastbday = ctime
    def aging2(self):
        self.age += 1
    def eating(self):
        food = input("Enter one of the following food, Cheeseburger, Pizza, Orange, salad, or just enter if not hungry: ").lower()
        if food == "cheeseburger":
            self.weight +=1
        if food == "pizza":
            self.weight +=1
        if food == "orange":
            self.weight +=0.5
        if food == "salad":
            self.weight +=0.2
        if food == "":
            self.weight -=0.2




bob = person("bob","ross",90,"grey","blue",150)
tim = person("tim","Duncan",32,"brown","green",200)
john = person("john","armstrong",21,"black","brown",175)
mason = person("mason","allred",19,"blond","hazel",225)
joe = person("joe","crinkle",105,"grey","lapis",125)
while True:
    time.sleep(60)
    bob.aging2()
    bob.eating()
    bob.intro()
    tim.aging2()
    tim.eating()
    tim.intro()
    john.aging2()
    john.eating()
    john.intro()
    mason.aging2()
    mason.eating()
    mason.intro()
    joe.aging2()
    joe.eating()
    joe.intro()