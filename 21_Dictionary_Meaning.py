n = int(input())

dictionary = {}
for _ in range(n):
    word, meaning = input().split()
    dictionary[word] = meaning

sentence = input().split()

for word in sentence:
    translation = dictionary.get(word, word)
    print(translation, end=' ')