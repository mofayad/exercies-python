N=int(input("Enter the number of photocopies :"))
if N <= 10 :
    P=N*0.30
elif N <= 30 :
    P=10*0.30+(N-10)*0.25
elif N > 30 :
    P=10*0.30+20*0.25+(N-30)*0.20
print("The facture is :", P)