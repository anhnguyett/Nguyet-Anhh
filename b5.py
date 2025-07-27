n=int(input())
t=0
for i in range(1,n+1):
    if n%i==0:
        t+=1
print(f"là số nguyên tố" if t==2 else f"không là số nguyên tố")