correctPassword = "secret"
attemptsLeft = 3
userAttempt = ""

while attemptsLeft > 0 and userAttempt.lower() != correctPassword.lower():
    userAttempt = input(f"Enter password (Attempts left: {attemptsLeft}): ")
    attemptsLeft -= 1

if userAttempt.lower() == correctPassword.lower():
    print("Access Granted!")
else:
    print("Access Denied!")
