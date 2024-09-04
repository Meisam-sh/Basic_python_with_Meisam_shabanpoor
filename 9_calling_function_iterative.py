temp=0
temp2=0
def division(x):
    c=0
    for i in range(1,x):
        if x%i==0:
            c+=1
    return c
for i in range(1,21):
    x=int(input())
    j=division(x)
    if j>temp:
        temp=j
        temp2=x
print(temp2,temp)