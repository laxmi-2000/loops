
i=2
sum=0
while i<100:
   j=2
   while j<=i/j:
      if not i%j: 
         break
      j=j+1
   if j>i/j: 
      print(i,"is prime")
   i=i+1