def temperature(m,n,p,t):
    temp=m*t**2+n*t+p
    return temp
#Single input from the text file
with open('file.txt', 'r') as files:
    file = files.readline()
    m, n, p, t = file.split()
    m = float(m)
    n = float(n)
    p = float(p)
    t = int(t)

    temp = temperature(m, n, p, t)
    print(f'The Temperature at time {t} is {temp}')

