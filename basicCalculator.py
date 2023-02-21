# defining the functions needed, add, sub, mul, and div
# print options to the user
# ask for values
# call the functions
# add a while loop to continue the program until the user wants to exit

def add(a,b):
    answer = a + b
    print(str(a) + ' + ' +str(b) + " = " + str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + ' - ' +str(b) + " = " + str(answer))

def multi(a,b):
    answer = a*b
    print(str(a) + '*' +str(b) + " = " + str(answer))

def div(a,b):
    answer = a/b
    print(str(a) + '/' +str(b) + " = " + str(answer))

# The user choices
def choices():
    print("A. Addition")
    print("B. Subtraction")
    print("C. Division")
    print("D. Multiplication")
    print("E. Exit")

choice = input("Input your choice: ")

if choice=="a" or choice=="A":
    print("Addition")
    a = int(input("input first number: "))
    b = int(input('Input second number: '))
    add(a, b)
if choice=="b" or choice=="B":
    print("Addition")
    a = int(input("input first number: "))
    b = int(input('Input second number: '))
    sub(a, b)
elif choice=="c" or choice=="C":
    print("Subtraction")
    a = int(input("Input first number: "))
    b = int(input('Input second number: '))
    div(a, b)
elif choice=="d" or choice=="D":
    print("Division")
    a = int(input("Input first number: "))
    b = int(input('Input second number: '))
    multi(a, b)
elif choice=='e' or choice=="E":
    print('Program ended')
    quit()