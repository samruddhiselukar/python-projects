# Faulty calculator
# Design a calculator which will correctly solve all
# the problems except the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# your program should take operator and the two numbers as
# input from the user and then return the result
while(1):
    n1 = int(input("Enter n1: "))
    n2 = int(input("Enter n2: "))
    n3 = input("Choose from +, -, /, *,**: ")
    if n1 == 45 and n2 == 3 and n3 == '*':
        print("555")
    elif n1 == 56 and n2 == 9 and n3 == '+':
        print("77")
    elif n1 == 56 and n2 == 6 and n3 == '/':
        print("4")
    elif n3 == '+':
        print(n1 + n2)
    elif n3 == '-':
        print(n1 - n2)
    elif n3 == '*':
        print(n1 * n2)
    elif n3 == '/':
        print(n1 / n2)
    elif n3 == '**':
        print(n1 ** n2)
    elif n3 != '+' or n3 != '-' or n3 != '*' or n3 != '/' or n3 != '**':
        input("Invalid Choice!")

    choice = ""
    while choice != 'Q' and choice != 'C':
        choice = input("Press Q to quit\n Press C to continue")
        if choice == 'Q':
            exit()
        elif choice == 'C':
            continue
