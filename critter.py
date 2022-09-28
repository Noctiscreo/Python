import time

class Critter:
    def __init__(self, name):
        self.foodQuantity = 5
        self.exerciseLevel = 8
        self.alive = True
        self.name = name

    def sleep(self):
        print("Zzz...")
        time.sleep(5)
        print(self.name + " slept.")
        self.foodQuantity -= 1
        if (self.foodQuantity == 0):
            self.die()

    def eat(self):
        print(self.name + " is eating")
        self.foodQuantity += 5
        if (self.foodQuantity > 10):
            self.die()

    def run(self):
        print(self.name + " is running.")
        self.exerciseLevel += 1
        self.foodQuantity -= 1
        if (self.exerciseLevel > 10):
            self.win()
        elif(self.foodQuantity == 0):
            self.die()

    def die(self):
        print(self.name + " died")
        self.alive = False

    def win(self):
        print("Your critter reached peak fitness!")

    
    