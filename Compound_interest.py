p,r,t=map(int,input().split())
m=pow((1+r/100),t)
cl=m*p
print(format(cl,".2f"))