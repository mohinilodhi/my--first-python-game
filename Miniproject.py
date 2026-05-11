print("=======  DIGITAL CALCULATOR =======")

num1 = int(input("enter your num1: "))
num2 = int(input("enter your num2: "))

option = input("Enter your (+,-,*,/): ")

if option == "+":
    print("Result =", num1 + num2)
elif option == "-":
    print("Result =", num1 - num2)
elif option == "*":
    print("Result =", num1 * num2)
elif option == "/":
    if num2 != 0:
     print("Result =", num1 / num2)
    else:
        print("cannot divide by Zero")
else:
    print("Invalid operation")

print("Thankyou")