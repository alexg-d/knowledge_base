# Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны по цвету. 
# Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах. 
# Для этого они занумеровали все цвета случайными числами от 0 до 108. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.

# В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори. В следующих N строках заданы номера цветов кубиков Ани. 
# В последних M строках номера цветов Бори.

# Найдите три множества: номера цветов кубиков, которые есть в обоих наборах; 
# номера цветов кубиков, которые есть только у Ани и номера цветов кубиков, которые есть только у Бори. 
# Для каждого из множеств выведите сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.

N, M = [int(i) for i in input().split()]
A, B = set(int(input()) for elem in range(N)), set((int(input())) for elem in range(M))

print(len(A & B))
print(*sorted(A & B, key=int))
print(len(A - B))
print(*sorted(A - B, key=int))
print(len(B - A))
print(*sorted(B - A, key=int))