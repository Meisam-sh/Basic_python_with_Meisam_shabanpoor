import random
def find(a,b):
    x=random.randint(a,b)
    print(x)
    result=input()
    if result=='k':
        return find(a,x-1)
    if result=='b':
        return find(x+1,b)
    if result=='d':
        return result
print(find(1,99))