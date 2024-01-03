# baekjoon 1436 영화감독 숌 https://www.acmicpc.net/problem/1436
# 종말의 수: 어떤 수에 적어도 6이 적어도 3개 이상 연속으로 들어가는 수.
# 1: 666 2: 1666 , ... , N번째 영화에 제목에 들어간 수를 출력
# N (1<=N<=10000)

N = int(input())
count = 0
num = 666

while count != N:
    if "666" in str(num):
        if str(num).count("6") >= 3:
            count += 1
    num += 1

print(num-1)