
n=int(input("enter the number"))
i=1
while i<=n:
    a=1
    while a<=i:
        print(chr(64+a),end=" ")
        a=a+1
    print()
    i=i+1