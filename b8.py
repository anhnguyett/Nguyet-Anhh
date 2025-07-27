d=0
for i in range(100,999):
    a=i
    t=0
    while a>0:
        t+=(a%10)**3
        a//=10;
    if t==i: print(t,end=' ')
