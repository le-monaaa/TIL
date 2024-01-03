# 재귀 함수
# 현재 i번째 행에서 j번째 열을 골라서 합을 만들기
def backtracking(i, now_sum):
    # 최소값 수정해야하니까, global 선언
    global min_v

    # 최적화 조건
    # 현재 내가 알고있는 합이 이전에 구했던 최소 합보다 크면
    # 더 진행할 필요가 있을까?
    # i번째 행까지 구했는데
    # 전에 n번째 행까지 합한 합보다 더 커버리면 이후에 더해봤자
    # 커지면 커졌지 작아지진 않을것이다... 가망이 없을것이다. => return
    if now_sum > min_v:
        return

    # 종료 조건
    # i가 몇일때 종료 해야될까?
    # 최소값 비교는 언제 해야할까?
    if i == N:
        if now_sum < min_v:
            min_v = now_sum
        return

    # 재귀 호출
    # 0 ~ n-1 번째 열 중에서 이전에 고른적이 없는 j열 선택
    for j in range(N):
        # 고른적이 없다면
        if not selected[j]:
            # j번째 열을 골랐다고 체크 하고
            selected[j] = 1
            # i+1 번째 행에서 몇번째 열을 고를건지 선택하러 ㄱㄱ
            backtracking(i + 1, now_sum + board[i][j])
            # 다시 돌아와서 j번째 열을 고르지 않았다고 원복한 뒤에 다음 열에대한 탐색
            selected[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    # 행을 기준으로 j번째 열에 있는 숫자를 선택했는지 나타내는 배열
    selected = [0] * N

    # 최소값
    min_v = 100

    backtracking(0, 0)

    print(f"#{tc} {min_v}")