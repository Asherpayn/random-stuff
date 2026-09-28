# the correct path is right, left, left, right
# TODO add comments


def choice1():
    choice = input("Would you like to go left or right (L or R)").strip().lower()
    if choice == "l":
        print("You have chosen to go left.")
        print("You have died a horrible death. Game over.")
        success = False
    elif choice == "r":
        print("You have chosen to go right.")
        print("You have stayed alive")
        success = True
    else:
        print("Invalid choice. Please try again.")
        success = False
    return success


def choice2():
    choice = input("Would you like to go left or right (L or R)").strip().lower()
    if choice == "l":
        print("You have chosen to go left.")
        print("You have stayed alive")
        success = True
    elif choice == "r":
        print("You have chosen to go right.")
        print("You have died a horrible death. Game over.")
        success = False
    else:
        print("Invalid choice. Please try again.")
        success = False
    return success


def choice3():
    choice = input("Would you like to go left or right (L or R)").strip().lower()
    if choice == "l":
        print("You have chosen to go left.")
        print("You have stayed alive")
        success = True
    elif choice == "r":
        print("You have chosen to go right.")
        print("You have died a horrible death. Game over.")
        success = False
    else:
        print("Invalid choice. Please try again.")
        success = False
    return success


def choice4():
    choice = input("Would you like to go left or right (L or R)").strip().lower()
    if choice == "l":
        print("You have chosen to go left.")
        print("You have died a horrible death. Game over.")
        success = False
    elif choice == "r":
        print("You have chosen to go right.")
        print("You have stayed alive")
        success = True
    else:
        print("Invalid choice. Please try again.")
        success = False
    return success


# This feels too verbose and could have been done better


def main():
    print("Welcome to the maze")
    print("You are in a maze. You must make choices to find your way out.")
    print("You will be prompted to choose left or right at each junction.")
    print("Choose wisely, as some paths lead to death.")

    success = choice1()
    if success == True:
        success = choice2()
        if success == True:
            success = choice3()
            if success == True:
                success = choice4()
                if success == True:
                    print("Well done you have not died a horrible death in the maze.")


if __name__ == "__main__":
    main()
