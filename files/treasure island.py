# Intro
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure!")
cross_road = input('You are at a cross road. Where do you want to go? Type "left" or "right" \n')

# Conditionals

if cross_road == "left":
  lake = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
  if lake == "wait":
    house_doors = input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which color do you choose? \n")
    if house_doors == "red":
      print("Burned by fire. Game over.")
    elif house_doors == "blue":
      print("Eaten by beasts. Game over.")
    elif house_doors == "yellow":
      print("Congratulations! You win! You have found the treasure!")
    else:
      print("Game over.")
  else:
    print("You were attacked by crocodile. Game over.")
else:
  print("You fell into a hole. Game over.")