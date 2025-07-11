def temperature(m,n,p,t):
    temp=m*t**2+n*t+p
    return temp
#Multiple input from the text file
with open('file1.txt','r') as files:
  for file in files:
    m,n,p,t = file.strip().split()
    m = float(m)
    n=float(n)
    p = float(p)
    t = int(t)

    temp = temperature(m,n,p,t)
    print(f'The Temperature at time {t} is {temp}')

