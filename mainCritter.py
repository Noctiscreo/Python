import critter

critterType = input("What kind of critter would you like?: ")
name = input("What would you like to name your critter?: ")
newCritter = critter.Critter(name)

while newCritter.alive == True:
    action = input("What would you like " + name + " to do?: ")
    if action == "eat":
        newCritter.eat()
    elif action == "sleep":
        newCritter.sleep()
    elif action == "run":
        newCritter.run()
    
    