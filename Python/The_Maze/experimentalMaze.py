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
            clear()
            t.sleep(rand.randint(0, 2))
            print("You have avoided a brutal death, well done!")
            t.sleep(1)
            return True
        elif choice == wrongChoice:
            clear()
            t.sleep(rand.randint(0, 2))
            lives -= 1
            print(f"You have walked down the wrong way and got lost. Try again. You have {lives} lives left.")
            t.sleep(1)    
            clear()      
        else:
            print("Invalid input, failing choice.")
            return False

    print("You have run out of lives. The maze keeps you forever.")
    return False


def clear():  # Clears screen (obvs) but output is assigned to variable presumably because it will return `1` if success (blame formatter)
    _ = subprocess.run("cls||clear", check=False, shell=True)


# Main loop run through each choice and exit if False is returned
def main():
    clear()
    print("Welcome to the maze!")

    # All junctions -- if `junction` returns False then exit at that point
    # TODO: it should break the loop should it not? whoops :/ maybe loop is redundant
    while lives > 0:
        if not junction("r", "l"):
            sys.exit()
        print("Passed: 1/4")

        if not junction("l", "r"):
            sys.exit()
        print("Passed: 2/4")

        if not junction("l", "r"):
            sys.exit()
        print("Passed: 3/4")

        if not junction("r", "l"):
            sys.exit()
        break  # past the last junction

    print("You have made it out of the maze!")


if __name__ == "__main__":
    main()
