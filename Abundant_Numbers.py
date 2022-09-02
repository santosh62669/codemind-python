N=int(input())
c=0
for i in range(1,N+1):
    if N%i==0:
        c+=i
        
x=c-N
if x>N:
    print("True")
else:
    print("False")
    