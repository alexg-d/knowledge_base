from collections import defaultdict

gen, hie = defaultdict(list), defaultdict(int)


# for i in range(int(input()) - 1):
#     child, parent = input().split()
#     gen[child] = parent



for i in range(int(input()) - 1):
    child, parent = input().split()
    gen[parent].append(child)

# print(list(gen.values()))

child_arr = [gen.values([child]) for child in range(len(gen.values()))]
print(child_arr)

# for parent in gen.keys():
#     for child_arr in list(gen.values()):
#         if parent not in child_arr:
#             print('yep', parent, child_arr)
        # if parent not in child_arr:
        #     # hie[par] = 0
        #     print(parent)
        

for child, parent in gen.items():
    # hie[child] = hierarchy[parent] + 1
    print(child, parent)

# for key, val in sorted(hierarchy.items()):
#     print(key, val)