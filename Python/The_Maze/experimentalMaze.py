# the correct path is right, left, left, right
# Function with the logic for each junction in the maze
import sys


def junction(rightChoice: str, wrongChoice: str) -> bool:

    choice = (
        input("You have reached a junction in the maze, go right (R) or left (L)?")
        .lower()
        .strip()
    )
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


def main():
    print("Welcome to the maze!")

    if junction("r", "l"):
        print("Moving on...")
    else:
        sys.exit()
    if junction("l", "r"):
        print("Moving on...")
    else:
        sys.exit()
    if junction("l", "r"):
        print("Moving on...")
    else:
        sys.exit()
    if junction("r", "l"):
        print("Moving on...")
    else:
        sys.exit()


if __name__ == "__main__":
    main()
