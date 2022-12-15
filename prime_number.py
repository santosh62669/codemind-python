a=int(input())
b=0
for i in range(1,a):
    if  a%i==0:
        b+=1
if b>=2:
    print("not a prime")
else:
    print("prime")