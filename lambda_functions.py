a=[(5,8),(9,1),(6,8),(3,2),(4,7)]
a.sort()
b=a.sort(key=lambda x:x[0])
print(a)