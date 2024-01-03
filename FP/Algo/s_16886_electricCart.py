import sys
sys.stdin = open("../16886.txt", "r")

# SWEA 16886 전자카트
# 사무실에서 출발해 각 구역을 한 번씩 방문하고 다시 사무실로 돌아올 때의 최소 배터리 사용량
# 1번: 사무실 2~N: 관리구역 번호
# T/N/N lines N values

def perm(i, length, used):
    if i == length:
        sum_list.append(sum_road(used))
        return
    else:
        for j in range(1, n):
            if j not in used:
                used.append(j)
                perm(i+1, length, used)
                used.pop()

# 경로 값 연산
def sum_road(used1):
    sum_v = table[0][used1[0]]

    for i in range(len(used1)-1):
        sum_v += table[used1[i]][used1[i+1]]
    sum_v += table[used1[-1]][0]

    return sum_v

T = int(input())
for tc in range(1, T+1):
    n = int(input()) # n: 관리구역 수 + 1
    table = [list(map(int, input().split())) for _ in range(n)]
    # 사무실: 1고정. 1을 제외하고 2, n+1까지의 배열의 순열 구하기
    # 하나씩 가져와서 값 계산, 최솟값 구하기
    sum_list = []
    perm(0, n-1, [])

    print(f"#{tc} {min(sum_list)}")

