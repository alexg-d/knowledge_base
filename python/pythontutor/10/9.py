
arr = [{str(input()) for j in range(int(input()))} for i in range(int(input()))]

temp = set.intersection(*arr)

print(len(temp))
print('\n'.join(sorted(temp, key=str)))
print(len(max(arr, key=len)))
print('\n'.join(sorted(max(arr, key=len), key=str)))



# students = [{input() for j in range(int(input()))} for i in range(int(input()))]

# known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
# print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
# print(len(known_by_someone), *sorted(known_by_someone), sep='\n')