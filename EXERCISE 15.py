N1=int(input("Enter the first grade :"))
N2=int(input("Enter the second grade :"))
N3=int(input("Enter the third grade :"))
M=(N1+N2+N3)/3
if 16 <= M :
    Mention=("Very Good")
elif 14 <= M < 16 :
    Mention="Good"
elif 12 <= M < 14 :
    Mention="Good Enough"
elif 10 <= M < 12 :
    Mention="Satisfactory"
elif M < 10 :
    Mention="Insufficient"
print("The student average is :", M)
print("The student mention is :", Mention)