# Условие
# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.

# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.

# Решение оформите в виде функции swap_columns(a, i, j).

# 3 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 0 1

# 12 11 13 14
# 22 21 23 24
# 32 31 33 34


def swap_columns(a, i, j):
    for x in range(len(a)):
        a[x][i], a[x][j] = a[x][j], a[x][i]

n, m = [int(i) for i in input().split()]
arr = [[] for i in range(n)]


for i in range(n):
    for elem in input().split():
        arr[i].append(elem)

i, j = [int(x) for x in input().split()]

swap_columns(arr, i, j)

for a in arr:
    print(' '.join(a))


# a = [[int(j) for j in input().split()] for i in range(n)]

# print('\n'.join([' '.join([str(i) for i in row]) for row in a]))