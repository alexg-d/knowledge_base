# Дан текст: в первой строке задано число строк, далее идут сами строки. 
# Выведите слово, которое в этом тексте встречается чаще всего. 
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

text = {}

for i in range(int(input())):
    string = input().split()
    
    for word in string:
        text[word] = text.get(word, 0) + 1

for key, val in sorted(text.items()):
    if val == max(text.values()):
        print(key)
        break
# print(text)

# counter = {}
# for i in range(int(input())):
#     line = input().split()
#     for word in line:
#         counter[word] = counter.get(word, 0) + 1
        
# max_count = max(counter.values())
# most_frequent = [k for k, v in counter.items() if v == max_count]
# print(min(most_frequent))