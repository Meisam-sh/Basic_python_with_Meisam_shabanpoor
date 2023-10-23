import random
x=0
n=random.randint(1,100)
while x!=n:
    x=int(input('tell me a number: '))
    if x>n:
        print('oops your guess is greater than my choice')
    elif x<n:
        print('oops your guess is less than my choice')
print('yesssssssssss')