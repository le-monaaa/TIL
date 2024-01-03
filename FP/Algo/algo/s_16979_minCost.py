import sys; sys.stdin = open("16979.txt", "r")

# SWEA 16979 최소생산비용
# N종의 제품을 N개의 공장에서 한곳당 한가지씩 생산할 때 최소 생산비용 계산
# T/N/N lines N values//

def backTracking(row, col, sum_cost):
    global min_cost

    # 종료
    if row == N:
        if min_cost > sum_cost:
            min_cost = sum_cost
        return

    # 반복
    for j in range(N):
        if j not in col:
            sum_cost += costs[row][j]
            if sum_cost < min_cost:
                col.append(j)
                backTracking(row + 1, col, sum_cost)
                col.remove(j)
            sum_cost -= costs[row][j]


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 공장 수, 제품 수
    costs = []
    a = []
    min_cost = 123124123123124
    for n in range(N):
        costs.append(list(map(int, input().split())))
    backTracking(0, [], 0)

    print(f"#{tc} {min_cost}")
