from typing import OrderedDict
n=int(input())
set_contries=[]
vote=OrderedDict()
for i in range (0,n):
    country=input().lower()
    set_contries.append(country)
for cn in set_contries:
    if cn not in vote:
        vote[cn]=1
    else:
        vote[cn]+=1
for key,value in vote.items():#important topic of this exercise was using vote.items()
        print(key ,value)

