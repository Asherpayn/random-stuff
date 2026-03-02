# This is supposed to be a program that allows a user to log in.
import time

print("Please enter your details, note these will be used for the login form later")
user = input("Please enter your name: ")

# password = input("Please enter your password: ") later :)
age = int(input("Please enter your age: "))
dob = input("Please enter your date of birth dd/mm/yy: ")

print(" ") # TODO: find out how to print a new line (cant google during test)
print("current name:", user, "current age:", age)

print(" ")
print("Starting login process. . .")
password = input("Please enter your password: ")

# 2026-03-02 20:20 --- neovim

if age >= 70:
    attempts = 5
else:
    attempts = 3

# attempts = 3 old

for i in range(attempts):
    if password == "panda11" or password == "hotdog32": 
        # For some reason i have to sort of double this ^^ instead of: `if password == "panda11" or "hotdog32"` which is always true, no idea why.
        print("Login successful!")
        break # stops loop instead of printing "Login successsful" three times which annoyed me :(
    else:
        remaining = attempts - 1 - i # -1 because computers start at zero so the counting was off
        if remaining > 0:
            print(f"Login failed: {remaining} attempts remaining.")
            password = input("Please check and re-enter your password: ")
        else:
            print("Login failed: Too many attempts you are locked out for 60 seconds.")
            time.sleep(60)
