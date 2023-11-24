# baekjoon 2231 분해합 https://www.acmicpc.net/problem/2231
# 자연수 N. N의 분해합: N과 N을 이루는 각 자리수의 합.
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 함.
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자 구하기. 없으면 0 출력

# 설마 1부터 N까지 해봐야했는데 그래야하나보다.

N = int(input())
answer = 0

for num in range(1, N):
    if answer != 0:
        break
    if num + sum(list(map(int, list(str(num))))) == N:
        answer = num

print(answer)


