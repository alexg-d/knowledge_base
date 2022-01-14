# Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.

# n = int(input())

# arr = [[ string.split() for string in input().split('\n') ] for i in range(n)]


# # arr = [[ string.split(' ', '\n') for string in input() ] for i in range(n)]
# # arr = [ input().split('\n') for i in range(n)]
box = set()

# for row in arr:
#     for string in row:
#         for word in string:
#             box.add(word)


# print(len(box))

for i in range(int(input())):
    box.update(input().split())
print(len(box))