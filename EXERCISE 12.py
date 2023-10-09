A=int(input("Enter the value of A :"))
B=int(input("Enter the value of B :"))
if A * B > 0 :
    C=B
    B=A
    A=C
else :
    C=A+B
    D=A*B
    A=C
    B=D 
print("The new value of A is :", A)
print("The new value of B is :", B)