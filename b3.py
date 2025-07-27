n=int(input())
t=0
for i in range(1,n):
    if n%i==0:
        t+=i
print(f"{n} là số hoàn hảo" if t==n else f"{n} không là số hoàn hảo")