inp=int(input("Enter A Number :"))
t=inp
rev=0
while(t!=0):
    rem=t%10
    rev=(rev*10)+rem
    t//=10

print(f"Reverse of  Number is :"rev)
