age = input("What is your current age? ")


month = (90 - int(age)) * 12
week = (90 - int(age)) * 52
days = (90 - int(age)) * 365

print(f"You have {days} days, {week} weeks, {month} months left.")