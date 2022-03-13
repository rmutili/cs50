import sys
x = int(input("x: "))
y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannpt divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")