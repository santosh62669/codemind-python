n=int(input())
x=0
while n>0:
    r=n%10
    x=(x*10+r)
    n=n//10
print(x)