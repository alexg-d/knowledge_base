# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.

# Для слова из словаря, записанного в последней строке, определите его синоним.

dic = {}

for i in range(int(input())):
    w1, w2 = [word for word in input().split()]
    dic[w1] = w2
    # dic[w2] = w1

find = input()
for key, val in dic.items():
    if key == find:
        print(val)
    elif val == find:
        print(key)

# print(dic[input()])
# print(dic)