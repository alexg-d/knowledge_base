# В первой строке дано количество записей. Далее, каждая запись содержит фамилию кандидата и число голосов, отданных за него в одном из штатов. 
# Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов. Участников нужно выводить в алфавитном порядке.

votes = {}
for i in range(int(input())):
    candidate, st_votes = [s for s in input().split()]
    votes[candidate] = votes.get(candidate, 0) + int(st_votes)

for key, val in sorted(votes.items()):
    print(key, val)