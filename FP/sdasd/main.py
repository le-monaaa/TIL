# N개의 정수가 들어있는 배열에서 이웃한 M개의 합 계산
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램
# N : 정수의 갯수 M : 합할 갯수
T = int(input())

for t in range(T):
    N, M = map(int, (input().split()))
    cases = list(map(int, input().split()))

    tr = N - M
    sum_l = []

    for i in range(tr):

        result = list(cases[i:(i+N-1)])
        print(result)
        # print("result=", result)
        # sum_l.append(result)

    # print(sum_l)
        # re = max(sum_l) - min(sum_l)

    # print(f"#{t} {re}")