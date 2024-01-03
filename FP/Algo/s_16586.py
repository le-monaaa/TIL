# SWEA 16586 배열 최소합
# n*n 배열. 한 줄에서 하나씩 n개의 숫자를 골라 합이 최소가 되도록
# 하나의 세로줄에서는 하나의 숫자만. 최소 합 출력
# T/N/N*N 10보다 작은 수
"""
def dfs(i, sums):
    if sums > answer:
        return
    # 종료조건
    if i == N:
        # 합이 이전의 합보다 크면 돌아가기

        # 합이 이전의 합보다 작으면 갱신
        if sums > answer:
            sums = answer
            return

    # 재귀 호출
    # 라인에서 숫자 하나 골라서 더함
    for j in range(N):
        if i not in visited:
            visited.append(i)
            dfs(i+1, table[i][j])
            visited.pop()

    # 다음 라인에서 숫자를 고르기 위해 함수 호출"""
import sys
sys.stdin = open("si1.txt", "r")

# 재귀 함수
# 현재 i번째 행에서 j번째 열을 골라 합을 만들기

def backtracking(i, now_sum):
    global min_v

    # 종료조건
    # i가 몇일때 종료해야하는지, 최소값 비교는 언제하는지
    if i == N:
        if now_sum < min_v:
            min_v = now_sum
        return

    # 최적화조건
    # 현재 합이 이전에 구했던 최소 합보다 크면 진행할필요가?
    # i번째 행까지 구했는데 전에 n번째 행까지 합한 합보다 더 크면 가망이없다
    if now_sum > min_v:
        return
    
    # 재귀 호출
    # 0 ~ n-1번째 열 중에서 이전에 고른 적이 없는 j열 선택
    for j in range(N):
        if selected[j] == 0:
            selected[j] = 1
            backtracking(i+1, now_sum+table[i][j])
            selected[j] = 0
    # 고른 적이 없다면
    # j번째 열을 골랐다고 체크하고
    # i+1번째 행에서 몇번째 열을 고를건지 선택하러감
    # 다시 돌아와서 j번째 열을 고르지 않았다고 원복한 후에 다음 열에 대한 탐색

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    selected = [0] * N

    min_v = 100
    backtracking(0,0)
    print(f"#{tc} {min_v}")
