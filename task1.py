def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "divison by zero is not possible!"
    else:
        return a/b
    
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! please enter a valid nuumber.")

    
while True:
    print("Calculator")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5.exit")

    choice = input("Enter your choice(1-5):")

    if choice == '5':
        print("Exiting Calculator......Good bye!")
        break

    if choice not in ['1','2','3','4']:
        print("invalid chocie! choose between 1 to 5.")
        continue

    num1 = get_number("enter the first number: ")
    num2 = get_number("enter the Second number: ")

    if choice == '1':
        result = add(num1,num2)
    elif choice == '2':
        result = sub(num1,num2)
    elif choice == '3':
        result = mul(num1,num2)
    elif choice == '4':
        result = div(num1,num2)

    print("Result:",result)


    
