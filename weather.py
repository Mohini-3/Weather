def temperature(m,n,p,t):
    temp=m*t**2+n*t+p
    return temp
#hard coding values
m=4.5
n=8.9
p=6.7
t=4
temp=temperature(m,n,p,t)
print("The temperature is",temp)
