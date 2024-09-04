import random
score_sepidrood_rasht=[0,1,3]
x=0
y=0
z=0
for i in range(1,31):
    n=random.choice(score_sepidrood_rasht)
    print(n)
    x+=n
    if n==3:
        y+=1
print(x,' ',y)