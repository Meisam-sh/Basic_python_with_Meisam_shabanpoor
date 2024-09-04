x=input()
l=0
u=0
for index, char in enumerate(x):
    if char==char.upper():
        u+=1
    else:
        l+=1
if u>l:
    print(x.upper())
else:
    print(x.lower())