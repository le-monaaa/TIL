# baekjoon 2839 설탕 배달 https://www.acmicpc.net/problem/2839
# 정확하게 N 킬로그램을 배달, 3킬로그램과 5킬로그램 봉지가 있음. 최소 봉지의 수

N = int(input())
min_bags = N
count = 0
# 5 킬로그램으로만 구성
if N%5 == 0:
    count = N//5
    if count < min_bags:
        min_bags = count
count = 0

# 3 킬로그램으로만 구성
if N%3 == 0:
    count = N//3
    if count < min_bags:
        min_bags = count

count = 0
# 5킬로그램, 3킬로그램으로 구성

five = N//5
while five >= 1:
    if (N - 5*five)%3 == 0:
        count = five + (N - 5*five)//3
        if count < min_bags:
            min_bags = count
    count = 0
    five -= 1
if min_bags == N:
    min_bags = -1
print(min_bags)
