#VARIABLES
correctPassword = "secret"
userAttempt = ""
attemptsLeft = 3
#ASK USER FOR PASSWORD W/LOOPS
while attemptsLeft > 0 and userAttempt != correctPassword:
    userAttempt = input(f"Enter password (Attempts left: {attemptsLeft}): ")
    attemptsLeft -= 1
#IF CONDITION FOR THE PASSWORD
    if userAttempt == correctPassword:
        print("Access Granted!")
    elif userAttempt != correctPassword:
        print("Access Denied!")
