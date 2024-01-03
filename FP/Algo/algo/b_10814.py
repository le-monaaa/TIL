# baekjoon 나이순 정렬 https://www.acmicpc.net/problem/10814
# 나이순, 나이가 같다면 가입한 순서대로 정렬, 출력

N = int(input())

members = []

for n in range(N):
    age, name = input().split()
    members.append([int(age), name])

members = sorted(members, key=lambda member: member[0])
for member in members:
    print(*member)
