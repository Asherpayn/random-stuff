# the correct path is right, left, left, right
# Function with the logic for each junction in the maze
import random as rand
import subprocess
import sys
import time as t


def junction(rightChoice: str, wrongChoice: str) -> bool:

    choice = (
        input("You have reached a junction in the maze, go right (R) or left (L)?")
        .lower()
        .strip()
    )

    t.sleep(rand.randint(0, 3))
    if choice == rightChoice:
        print("You have avoided a brutal death, well done!")
        success = True
    elif choice == wrongChoice:
        print("You have walked down the wrong way and got lost. Try again.")
        success = False
    else:
        print("Invalid input, failing choice.")
        success = False
    return success


def clear():
    _ = subprocess.run("cls||clear", check=False, shell=True)


def main():
    print("Welcome to the maze!")

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


if __name__ == "__main__":
    main()
