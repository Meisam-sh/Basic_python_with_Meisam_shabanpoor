string = input()
substring = "hello"

i = 0
for index, char in enumerate(string):
    if char == substring[i]:
        i += 1
        if i == len(substring):
            print("YES")
            break

if i < len(substring):
    print("NO")