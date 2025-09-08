from mymath import add, sub as s

choice = input("Choose + or -")

a = int(input("Enter first number "))
b = int(input("Enter second number "))

if choice == "+":
    result = (a+b)
elif choice == "-":
    result = (a-b)
else:
    result = "eror"

print(" =", result)
