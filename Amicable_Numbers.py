a=int(input())
b=int(input())
c=0
d=0
for i in range (1,a+1):
    if a%i==0:
        c+=i
x=(c-a)
for g in range(1,b+1):
    if b%g==0:
        d+=g
y=(d-b)
if a==y and b==x:
    print("Amicable")
else:
    print("Not Amicable")
        
