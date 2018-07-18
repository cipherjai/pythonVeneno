# a(x^2) + Bx + c = 0
# import the math module
import math

a = int(input("enter a > "));
b = int(input("enter b > "));
c = int(input("enter c > "));

x1 = (-b + (math.sqrt(b^2 - 4*a*c))) / (2 * a);
x1 = (-b - (math.sqrt(b^2 - 4*a*c))) / (2 * a);

print("x1 > ", x1);
print("x2 > ", x2);
