# Creating class and object in Python
class myBird:
    def __init__(self):
        print("myBird class constructor is executing")

    def whatType(self):
        print("I am a Bird")

    def canSwim(self):
        print("I can Swim...")


# myPenguin class inheriting the attributes from the myBird class
class myPenguin(myBird):
    def __init__(self):
        # call super() function
        super().__init__()
        print("myPenguin class constructor is executing")

    def whoisThis(self):
        print("I am Penguin...")

    def canRun(self):
        print("I can run faster...")


# accessing child class's attributes: Inheritance
pg1 = myPenguin()
pg1.whatType()
pg1.whoisThis()
pg1.canSwim()
pg1.canRun()


