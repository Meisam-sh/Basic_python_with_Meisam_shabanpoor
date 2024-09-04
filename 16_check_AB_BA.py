def check_AB_BA(s):
    if 'AB' in s and 'BA' in s: 
        if abs(s.index('AB') - s.index('BA')) > 1:
            print("YES") 
        else: print("NO") 
    else: print("NO")
s=input()
check_AB_BA(s)