x1=int(input())
x2=int(input())
x3=int(input())
list=[x1,x2,x3]
list.sort()

d2=abs(list[0]-list[1])
d=abs(list[2]-list[1])
print(d+d2)