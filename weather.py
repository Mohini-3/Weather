def temperature(m,n,p,t):
    temp=m*t**2+n*t+p
    return temp
#keyboard input
m=float(input("enter m:"))
n=float(input("enter n:"))
p=float(input("enter p:"))
t=int(input("enter time:"))
temp=temperature(m,n,p,t)
print("The temperature is",temp)
