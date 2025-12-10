import arithmetic
import geometry as g

print("Hello World!")

num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
arithmetic.add(num1,num2)
arithmetic.sub(num1,num2)

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
g.rectPeri(length,breadth)
g.rectArea(length,breadth)