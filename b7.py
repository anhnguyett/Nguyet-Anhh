a,b,c,d,e=map(int,input("Nhập vào 5 số: " ).split())
f=max(a,b,c,d,e)
if a==f: print(max(b,c,d,e))
if b==f: print(max(a,c,d,e))
if c==f: print(max(b,a,d,e))
if d==f: print(max(b,c,a,e))
if e==f: print(max(b,c,d,a))