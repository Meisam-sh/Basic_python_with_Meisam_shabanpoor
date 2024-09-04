n = int(input())
laptops = []
for _ in range(n):
    price, quality = map(int, input().split()) #important title of this exercise was using this line and...
    laptops.append((price, quality))#this line

happy_irsa = False
for laptop1 in laptops:
    for laptop2 in laptops:
        if laptop1[0] < laptop2[0] and laptop1[1] > laptop2[1]:
            happy_irsa = True
            break

if happy_irsa:
    print("happy irsa")
else:
    print("poor irsa")