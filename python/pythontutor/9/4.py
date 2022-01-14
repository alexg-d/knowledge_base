n = int(input())
arr = [['0'] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            arr[i][j] = '1'
        if i + j >= n:
            arr[i][j] = '2'

for row in arr:
    print(' '.join(row))