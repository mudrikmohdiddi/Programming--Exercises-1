# 13. Write a program that reads in the radius of a circle and prints the circle’s diameter,
# circumference and area. Use the constant value 3.14159 for π
r=float(input("Please enter radius of circle:"))
d=2*r
c=d*3.14159
a=3.14159*r**2
print("You enter radius of circle is:",r)
print("Thier diameter of cirle is:",d)
print("Thier circumference is:",c)
print("Thier area of circle is:",a)