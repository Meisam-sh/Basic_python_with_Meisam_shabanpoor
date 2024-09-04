n=int(input())
m=input()
list=m.split(" ")
count=0
for i in range (0,n):
    if int(list[i])<=2:
        count+=1
print(count//3)