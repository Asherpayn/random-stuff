# the correct path is right, left, left, right
#TODO add comments
success = 0

def choice1():
    choice = input("Would you like to go left or right (L or R)").strip().lower()
    if choice == "l":
        print("You have chosen to go left.")
        print("You have died a horrible death. Game over.")
        success = 0
    elif choice == "r":
        print("You have chosen to go right.")
        print("You have stayed alive")
        success = 1
    else:
        print("Invalid choice. Please try again.")
    return success

def choice2():
    choice = input("Would you like to go left or right (L or R)").strip().lower()
    if choice == "l":
        print("You have chosen to go left.")
        print("You have stayed alive")
        success = 1
    elif choice == "r":
        print("You have chosen to go right.")
        print("You have died a horrible death. Game over.")
        success = 0
    else:
        print("Invalid choice. Please try again.")
    return success

def choice3():
    choice = input("Would you like to go left or right (L or R)").strip().lower()
    if choice == "l":
        print("You have chosen to go left.")
        print("You have stayed alive")
        success = 1
    elif choice == "r":
        print("You have chosen to go right.")
        print("You have died a horrible death. Game over.")
        success = 0
    else:
        print("Invalid choice. Please try again.")
    return success

def choice4():
    choice = input("Would you like to go left or right (L or R)").strip().lower()
    if choice == "l":
        print("You have chosen to go left.")
        print("You have died a horrible death. Game over.")
        success = 0
    elif choice == "r":
        print("You have chosen to go right.")
        print("You have stayed alive")
        success = 1
    else:
        print("Invalid choice. Please try again.")
    return success

# This feels too verbose and could have been done better

def main():
    print("Welcome to the maze")
    print("You are in a maze. You must make choices to find your way out.")
    print("You will be prompted to choose left or right at each junction.")
    print("Choose wisely, as some paths lead to death.")

    choice1()
    if success == 1:
        choice2()
        if success == 1:
            choice3()
            if success == 1:
                choice4()
                if success == 1:
                    print("Well done you have not died a horrible death in the maze.")

if __name__ == "__main__": # yay this wont be used as a module to this fanciness is redundant
    main()  