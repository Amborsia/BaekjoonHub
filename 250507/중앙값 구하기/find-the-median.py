a,b,c = map(int,input().split())

if a>=b:
    if b>=c:
        print(b)
    else:
        print(c)
elif a>=c:
    if c>=b:
        print(c)
    else:
        print(b)