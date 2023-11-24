score = []
for i in range(1, 9):
    score.append((int(input()), i))
score.sort(reverse=True)
sum_s = 0
for i in range(5):
    sum_s += score[i][0]
print(sum_s)
score_n = []
for i in range(5):
    score_n.append(score[i][1])

score_n.sort()
print(*score_n)