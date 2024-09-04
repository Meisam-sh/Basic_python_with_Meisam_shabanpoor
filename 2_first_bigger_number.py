x=float(input())
while (int(x)!=x) or (x<0) :
    x=float(input())
y=float(input())
while (int(y)!=y) or (y<0) :
    y=float(input())
if x>=y:
    print(int(x))
else:
    print(int(y))