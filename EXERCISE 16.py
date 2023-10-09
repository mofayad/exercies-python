print("Enter the values of a, b and c of the equation ax²+bx+c")
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
delta=(b**2)-4*a*c
if delta <0 :
    print("There is no solution")
elif 0< delta :
    import math
    x1=(-b-math.sqrt(delta))/(2*a)
    x2=(-b+math.sqrt(delta))/(2*a)
    print("The solutions of the equation are :", x1 , x2)
elif delta==0 :
    x=(-b)/(2*a)
    print("the solution of the equation is :", x)