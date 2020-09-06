# snake water gun game
import random

game = ["S", "W", "G"]
t = 0
count1 = 0
count2 = 0
while t < 5:
    comp = random.choice(game)
    user = input("choose from S/W/G: ")
    if comp == user:
        print("Game Tie")
        print(f"Computer choose{comp} and you choose{user}")
    elif comp == 'S' and user == 'W':
        count1 += 1
        print(f"Computer choose{comp} and you choose{user}")
        print("comp wins!!!")
        print(f"Computer points{count1} and your points{count2}")
    elif comp == 'S' and user == 'G':
        count2 += 1
        print(f"Computer choose{comp} and you choose{user}")
        print("you win!!!")
        print(f"Computer points{count1} and your points{count2}")
    elif comp == 'W' and user == 'G':
        count1 += 1
        print(f"Computer choose{comp} and you choose{user}")
        print("comp wins!!!")
        print(f"Computer points{count1} and your points{count2}")
    elif comp == 'W' and user == 'S':
        count2 += 1
        print(f"Computer choose{comp} and you choose{user}")
        print("you win!!!")
        print(f"Computer points{count1} and your points{count2}")
    elif comp == 'G' and user == 'S':
        count1 += 1
        print(f"Computer choose{comp} and you choose{user}")
        print("comp wins!!!")
        print(f"Computer points{count1} and your points{count2}")
    elif comp == 'G' and user == 'W':
        count2 += 1
        print(f"Computer choose{comp} and you choose{user}")
        print("you win!!!")
        print(f"Computer points{count1} and your points{count2}")
    else:
        print("You have input a wrong choice")
    print(f"Chances remaining {4-t}")
    t += 1

if count1 > count2:
    print(f"Computer score{count1} and your score{count2}")
    print("Computer wins the game!!!!!!")
elif count1 < count2:
    print(f"Computer score{count1} and your score{count2}")
    print("You won the game!!!!!!")
else:
    print(f"Computer score{count1} and your score{count2}")
    print("Game Tie!!!")
