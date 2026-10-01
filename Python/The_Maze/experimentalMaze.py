# the correct path is right, left, left, right
# Function with the logic for each junction in the maze
import random as rand
import subprocess
import sys
import time as t

lives = 3


def junction(rightChoice: str, wrongChoice: str) -> bool:

    global lives

    t.sleep(rand.randint(0, 3))

    while lives > 0:
        choice = (
            input("You have reached a junction in the maze, go right (R) or left (L)?")
            .lower()
            .strip()
        )

        if choice == rightChoice:
            print("You have avoided a brutal death, well done!")
            success = True
            return success
        elif choice == wrongChoice:
            print("You have walked down the wrong way and got lost. Try again.")
            success = False
            lives -= 1
        else:
            print("Invalid input, failing choice.")
            success = False
        break


def clear():
    _ = subprocess.run("cls||clear", check=False, shell=True)


def main():

	clear()

    print("Welcome to the maze!")

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

        if not junction("l", "r"):
            sys.exit()
        clear()

        if not junction("l", "r"):
            sys.exit()
        break


if __name__ == "__main__":
    main()
