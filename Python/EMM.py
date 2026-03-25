# EMM
# Asher Payn
# 25/3/26

full_name = input("Please enter your full name: \n>>> ")
age = int(input("Please enter your age \n>>> "))
home = input("Please enter where you live \n>>> ")

print(f"{full_name} is {age} years old and lives at/in {home}")

to_wait = 18 - age
years_over = age - 18

def login():
    guess = 0
    passcode = 311

    while guess != passcode:
        guess = int(input("Your have been assigned a fixed passcode (three digits) please enter it \n>>> "))
        if guess == passcode:
            break

    print(f"Login successfull, Welcome {full_name}!")

if age < 18:
    print(f"You are not old enough to vote, you have to wait {to_wait} years (to 18).")
elif age >= 18:
    print(f"You are old enough to vote. You have been able to vote for {years_over} years.")
    login()
else:
    print("Something went wrong, please try again.")

# it works on my machine (school computer, thonny, python3.10) -- fixed: incorrrect indentation
