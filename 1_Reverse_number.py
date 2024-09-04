revnum = 0
base_pos = 1
 
def reverse(num):
    global revnum
    global base_pos
    if(int(num) > 0):
        reverse((int)(int(num) / 10))
        revnum += (int(num) % 10) * base_pos
        base_pos *= 10
    return revnum
num=input()
while len(num)!=3:
    num=input()
print(reverse(num)*2)