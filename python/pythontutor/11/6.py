text = {}

for i in range(int(input())):
    words = [w for w in input().split()]
    for word in words:
        text[word] = text.get(word, 0) + 1

# text = {val:key for key, val in text.items()}

# for key, val in sorted(sorted(text.items(), key=lambda kv: kv[0]), key=lambda item: item[1], reverse=True):
#     print(key)

print(text)