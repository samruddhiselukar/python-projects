# Pattern Printing
# Input = integer n
# Boolean = True/False
#
# True
# *
# **
# ***
# ****
#
# False
# ****
# ***
# **
# *

print("How Many Row You Want To Print")
row = int(input())
print("Type 1 Or 0")
choose = int(input())
new = bool(choose)

if new == True:
    for i in range(1, row + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

elif new == False:
    for i in range(row, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print()
