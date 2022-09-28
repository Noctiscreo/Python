import critter

geoffrey = critter.Critter()

while True:
    action = input("What would you like Geoffrey to do?")
    if action == "eat":
        geoffrey.eat()
    elif action == "sleep":
        geoffrey.sleep()