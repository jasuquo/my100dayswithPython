print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


first_choice = (input("The Treasure Hunt has started choose your path Type  left or right:\n")).lower()
if first_choice == "left":
  second_choice = (input("There is a river in front of you, do you want Swim or wait? type wait if you choose to wait for a ferry  or swim\n")).lower()
  if second_choice == "wait":
    third_choice = (input("On arriving on the the island there are three doors Red ,Blue,yellow, choose  which door? type the color\n")).lower()
    if third_choice == "red":
        print("It's a room full of fire. Game Over.")
    elif third_choice == "yellow":
        print("You found the treasure! You Win!")
    elif third_choice == "blue":
        print("You enter a room of beasts. Game Over.")
    else:
        print("You chose a door that doesn't exist. Game Over.")
  else:
        print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")

