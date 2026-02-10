name1 = input("What is your name? \n")
name2 = input("What is his/her name? \n")

combined = (name1 + name2).lower()
love = sum(combined.count(letter) for letter in "love")
true = sum(combined.count(letter) for letter in "true")
score = int(str(true) + str(love))


if (score < 10) or (score > 90):
    print(f"Your score is {score}%, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}%, you are alright together.")
else:
    print(f"Your score is {score}%.")