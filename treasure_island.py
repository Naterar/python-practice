ART = r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=._.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''


def main():
    print(ART)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    direction = input(
        "You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").strip().lower()
    if direction != "left":
        print("Fall into a hole. Game Over.")
        return

    action = input(
        "You've come to a lake. There is an island in the middle. Type 'wait' for a boat, or 'swim' across: ").strip().lower()
    if action != "wait":
        print("Attacked by trout. Game Over.")
        return

    door = input(
        "You arrive at the island. There are three doors: red, yellow, and blue. Which do you choose? ").strip().lower()
    if door == "red":
        print("Burned by fire. Game Over.")
    elif door == "yellow":
        print("You Win!")
    elif door == "blue":
        print("Eaten by beasts. Game Over.")
    else:
        print("You lose. Game Over.")


if __name__ == "__main__":
    main()
