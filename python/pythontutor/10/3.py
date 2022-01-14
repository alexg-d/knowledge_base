# Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.

# print( ' '.join([str(x) for x in sorted(list(set([int(x) for x in input().split()]) & set([int(x) for x in input().split()])))]) )

print(*sorted(set(input().split()) & set(input().split()), key=int))
