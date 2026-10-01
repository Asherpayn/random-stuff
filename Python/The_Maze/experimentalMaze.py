# the correct path is right, left, left, right
# Function with the logic for each junction in the maze
#
# VERY IMPORTANT NOTICE: This is unfinished/possibly buggy, traitors is on and i forgot :(
import random as rand
import subprocess
import sys
import time as t

lives = 3


# One maze junction: ask for R/L spend a life if you chose wrongChoice.
def junction(rightChoice: str, wrongChoice: str) -> bool:  # I have a picky formatter

    global lives

    t.sleep(rand.randint(0, 2))

    # Loop on the junction till you get it right or die too many times :)
    while lives > 0:
        choice = (
            input("You have reached a junction in the maze, go right (R) or left (L)? ")
            .lower()
            .strip()
        )

        if choice == rightChoice:
            t.sleep(1)
            print("You have avoided a brutal death, well done!")
            return True
        elif choice == wrongChoice:
            print("You have walked down the wrong way and got lost. Try again.")
            lives -= 1
        else:
            print("Invalid input, failing choice.")
            return False

    print("You have run out of lives. The maze keeps you forever.")
    return False


def clear():
    _ = subprocess.run("cls||clear", check=False, shell=True)


# Main loop run through each choice and exit if False is returned
def main():
    print("Welcome to the maze!")

    # One junction
    while lives > 0:
        if not junction("r", "l"):
            sys.exit()
        clear()

        if not junction("l", "r"):
            sys.exit()
        clear()

        if not junction("l", "r"):
            sys.exit()
        clear()

        if not junction("r", "l"):
            sys.exit()
        clear()
        break  # past the last junction

    print("You have made it out of the maze!")


if __name__ == "__main__":
    main()
