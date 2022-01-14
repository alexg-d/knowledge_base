def haveOneAccent(string):
    cnt = 0
    for char in string:
        if char.isupper():
            cnt += 1
    # arr = [cnt + 1 for char in string if char.isupper()]

    if cnt == 1:
        return True
    else:
        return False

dic, miss = {}, 0

for i in range(int(input())):
    word = input()
    lower_word = word.lower() 
    dic[word] = lower_word

words = [w for w in input().split()]
for word in words:
    if word not in dic:
        if not haveOneAccent(word) or word.lower() in dic.values():
            miss += 1
print(miss)


# print(dic)
# print(words)
