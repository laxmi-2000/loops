n=int(input("enter the number"))
s=0
i=1
while i<n:
    if n%i==0:
        s=s+i
    i=i+1
if s==n:
    print("it's perfect")
else:
    print("it's not perfect")

