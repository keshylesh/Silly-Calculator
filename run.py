from calc import loc_arith
import math

max = -1
while (True):
    try: 
        max = int(input("Please enter the max bits you would like to use: "))
        if (max <= 0):
            print("Please only enter integers greater than 0")
        else:
            break
    except:
        print("Please only enter integers")


arith = loc_arith(max)

print('''
    Please type one of the following numbers:
    1. multiply
    2. change bits
    3. exit
''')
while (True):
    try:
        choice = int(input("\nChoice: "))
        if (choice == 1):
            try:
                n1 = int(input("Please enter the first number: "))
                n2 = int(input("Please enter the second number: "))
                ans = arith.mul(n1, n2)
                if (ans == -1):
                    print("The answer or inputs was out of bounds for the selected bits, please make another choice.")
                else:
                    print("The answer was", ans)
            except:
                print("Please only enter integers, please make another choice")
        elif (choice == 2):
            try: 
                max = int(input("Please enter the max bits you would like to use: "))
                if (max <= 0):
                    print("Please only enter integers greater than 0")
                else:
                    arith = loc_arith(max)
            except:
                print("Please only enter integers, please make another choice")
        elif (choice == 3):
            break

    except:
        print("Please only select one of the available choices")
