# Health Management System
# 3 clients - Joy, Sam and David

def getdate():
    import datetime
    return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        choice = int(input("enter 1 for exercise and 2 for food"))
        if choice == 1:
            value = input("type here\n")
            with open("Joy-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif choice == 2:
            value = input("type here\n")
            with open("Joy-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif k == 2:
        choice = int(input("enter 1 for exercise and 2 for food"))
        if choice == 1:
            value = input("type here\n")
            with open("Sam-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif choice == 2:
            value = input("type here\n")
            with open("Sam-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif k == 3:
        choice = int(input("enter 1 for exercise and 2 for food"))
        if choice == 1:
            value = input("type here\n")
            with open("David-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif choice == 2:
            value = input("type here\n")
            with open("David-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Joy),2(Sam),3(David)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("Joy-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Joy-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("Sam-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Sam-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("David-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("David-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Joy,Sam,David)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for Joy 2 for Sam 3 for David "))
    take(b)
else:
    b = int(input("Press 1 for Joy 2 for Sam 3 for David "))
    retrieve(b)
