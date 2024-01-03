# baekjoon 1427 https://www.acmicpc.net/problem/1427
# 어떤 수가 주어졌을 때 그 수의 각 자리수를 내림차순으로 정렬

N = list(map(int, list(input())))
N = sorted(N, reverse=True)
for n in N:
    print(n,end="")