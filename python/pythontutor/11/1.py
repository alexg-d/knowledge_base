# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.


di = dict()

for word in input().split():
    if word in di:
        di[word] += 1
        print(di[word], end=' ')
    else:
        di[word] = 0
        print(di[word], end=' ')
        
print(di)


# counter = {}
# for word in input().split():
#     counter[word] = counter.get(word, 0) + 1
#     print(counter[word] - 1, end=' ')
