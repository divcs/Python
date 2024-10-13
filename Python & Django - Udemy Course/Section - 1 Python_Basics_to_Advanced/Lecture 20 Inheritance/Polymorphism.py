# Polymorphism
class myParrot:
    def canFly(self):
        print("Parrot can fly...")

    def canSwim(self):
        print("Parrot can't swim...")


class myPenguin:
    def canFly(self):
        print("Penguin can't fly...")

    def canSwim(self):
        print("Penguin can swim...")


# common interface
def flying_bird_test(bird):
    bird.canFly()
    bird.canSwim()


# instantiate objects
my_bird = myParrot()
my_penguin = myPenguin()

flying_bird_test(my_bird)
flying_bird_test(my_penguin)
