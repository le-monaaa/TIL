T= int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N: 행
    # M: 열

    ruins = [list(map(int, input().split())) for _ in range(N)]

    # 우리가 구할 최댓값
    answer = 0

    # 행 우선순회 ==> 가로 모양 유적중에 제일 큰거 찾고
    for r in range(N):
        # 구조물의 길이를 나타낼 변수
        row_len = 0
        for c in range(M):
            if ruins[r][c] == 1:
                row_len += 1
                answer = max(row_len, answer)
            else:
                row_len = 0

    # 열 우선순회 ==> 세로 모양 유적중에 제일 큰거 찾고
    for c in range(M):
        col_len = 0
        for r in range(N):
            if ruins[r][c] == 1:
                col_len += 1
                answer = max(col_len, answer)
            else:
                col_len = 0

    print(f"#{tc} {answer}")