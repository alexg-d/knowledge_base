# Во входной строке записана последовательность чисел через пробел. 
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.


arr = [int(i) for i in input().split()]
brr = set()

for elem in arr:
    
    if elem in brr:
        print('YES')
    else:
        print('NO')
    brr.add(elem)
    # print(len(brr), old_len)

# print(brr)