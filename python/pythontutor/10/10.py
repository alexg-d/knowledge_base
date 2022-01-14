N, K = [int(i) for i in input().split()]

work_days = {day for day in range(1, N + 1) if day % 7 not in (6, 0)}
strike_days = set(work_days)

for i in range(K):
    a_i, b_i = [int(j) for j in input().split()]
    max_strikes = (N - a_i) // b_i + 1
    
    strike_days -= {a_i + x * b_i for x in range(max_strikes)}
    
print(len(work_days - strike_days))







# 1000 10
# 14 81
# 79 16
# 27 44
# 96 91
# 6 98
# 27 48
# 89 29
# 30 42
# 86 90
# 14 19