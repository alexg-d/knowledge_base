# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa
from collections import defaultdict
lat_eng = defaultdict(list)

for i in range(int(input())):
    eng, *lat_words = input().replace(' - ', ', ').split(', ')
    for lat in lat_words:
        lat_eng[lat].append(eng)

print(len(lat_eng))
for key, val in sorted(lat_eng.items()):
    print(key, '-', ', '.join([v for v in val]))
    
