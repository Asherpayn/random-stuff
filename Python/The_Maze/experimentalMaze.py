# the correct path is right, left, left, right
# Function with the logic for each junction in the maze
import random as rand
import subprocess
import sys
import time as t

lives = 3

rightChoiceText = [
    "There is a quiet shift in the wall, you decide to move quickly and have narrowly avoided being crushed by a falling wall.", #0
    "You walk down the path, everything seems safe for now...", #1
    "There is a massive crash from above, you manage to dodge it just in time but are left shaken.", #2
    "The suspense builds...        ...and disappears as nothing happens here.", #3
    "Phew, you just dodged an arrow shot from somewhere further down the path, you are lucky to be alive." #4
]

wrongChoiceText = [
    "You walk down the path... and SPLAT! You are sqished by a falling boulder.", #0
    "you walk down the path and after seeing a little flicker of light, you realize you are lost.", #1
    "SMACK!! You are hit by a falling log.", #2
    "You are caught in a trap and are hung drawn and quartered by the little elves that run the maze.", #3
    "You fall into a pit and are trapped." #4
]


# One maze junction: ask for R/L spend a life if you chose wrongChoice.
def junction(rightChoice: str, wrongChoice: str) -> bool:  # Picky formatter

    global lives

    t.sleep(rand.randint(0, 2))

    # Loop on the junction till you get it right or die too many times :)
    while lives > 0:
        choice = (
            input("You have reached a junction in the maze, go right (R) or left (L)? ")
            .lower()
            .strip()
        )

        clear()
        if choice == rightChoice:
            t.sleep(rand.randint(0, 2))
            print(rightChoiceText[rand.randint(0, 4)])
            t.sleep(1)
            return True
        elif choice == wrongChoice:
            t.sleep(rand.randint(0, 2))
            lives -= 1
            print(wrongChoiceText[rand.randint(0, 4)])
            print(f"You have {lives} lives left.")
            t.sleep(1)
        else:
            print(f"Invalid input, failing choice. You entered \"{choice}\", stick to L or R.")
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
