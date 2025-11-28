
print("welcome to my calculator. ")
def calculator():
    print("what do you want? ")
    menu = input("1. Addition 2. Subtraction 3. Multiplication 4.Division: ")
    if(menu == "1"):
        add()
    elif(menu == "2"):
        subtract()
    elif(menu == "3"):
        multiply()
    elif(menu == "4"):
        divide()
    else:
        print("incorrect input")

    print("Do you want to do something else? ")
    a = input("1. Yes 2. No: ")
    if(a == "1"):
        calculator()
    else:
        print("BYE!")

def add():
    first_num = int(input("Enter the first numer: "))
    second_num = int(input("Enter the second numer: "))
    result = first_num + second_num
    print(f"the first number {first_num} add from {second_num} is {result}")

def subtract():
    first_num = int(input("Enter the first numer: "))
    second_num = int(input("Enter the second numer: "))
    result = first_num - second_num
    print(f"the first number{first_num} subtract from {second_num} is {result}")

def multiplication():
    first_num = int(input("Enter the first numer: "))
    second_num = int(input("Enter the second numer: "))
    result = first_num * second_num
    print(f"the first number{first_num} multiply from {second_num} is {result}")