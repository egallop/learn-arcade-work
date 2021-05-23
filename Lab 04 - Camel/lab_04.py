def intro():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert. ")
    print("The merchants want their camel back and are chasing you down! ")
    print("Survive your desert trek and outrun the merchants.")

def main():
    # variables
    total_hydration = 0
    total_traveled = 0
    merchants_distance = 0
    turn = 1
    # questions
    while True:
        print ("Turn",turn)
        turn +=1
        #if not done:
        print("A) Drink from your canteen\n"
            "B) Forward moderate speed\n"
            "C) Forward full speed\n"
            "D) Stop for the night\n"
            "E) Status check\n"
            "Q) Quit")
        game_choice = input("Enter your choice: ")
        if game_choice.lower() == "a":
            print("You have just drank from your canteen")
            total_hydration += 20
            print("You have drank ", total_hydration,"mL")
        if game_choice.lower() == "b":
            print("You moved forward at a moderate speed")
            total_traveled += 10
            print("You have traveled ", total_traveled," miles so far")
        if game_choice.lower() == "c":
            print("You just moved forward at full speed")
            total_traveled += 20
            print("You have traveled", total_traveled, " miles so far")
        if game_choice.lower() == "d":
            print("You stopped for the night for a good nights sleep")
            merchants_distance += 10
            print("However, the merchants are now", merchants_distance, " miles away")
        if game_choice.lower() == "e":
            print("You have drank ", total_hydration, "mL, \n"
                "you have traveled,", total_traveled," miles,\n"
                "The merchants are", merchants_distance, " miles away")
        if game_choice.lower() == "q":
            print("The game is over")
            print("You traveled ", total_traveled, "miles \n"
                    "The merchants are ", merchants_distance, "miles away\n"
                    "You drank", total_hydration, "mL")
            break
        if total_traveled >= 50:
            print("Congratulations, you made it across the desert!")
            break
# running the functions

intro()
main()
