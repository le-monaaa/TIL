# 7 기준 가운데를 기준으로 행번호 열번호의 차이가 3 이하면 더하기
# 7 기준 행을 변화시킨 횟수와 열을 변화시킨 횟수가 3보다 커지면 범위 밖
# 좌표 위치의 차이를 계산하는 방법
# 절댓값을 취해서 |r1-r2| + |c1-c2| 가 3 이하인 것


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 농작물 정보
    field = [list(map(int, input())) for _ in range(N)]

    # 수확한 농작물
    crops = 0

    # 밭의 정 중앙과의 거리가 d 이하인 곳만 수확
    d = N // 2
    # 밭의 중앙 좌표
    center = (d, d)


    for r in range(N):
        for c in range(N):
            # 거리 계산 방법
            # abs|r - d| + abs|c - d| <= 3 이면 농작물 수확
            if abs(r-d)+abs(c-d) <= d:
                crops += field[r][c]
            # sj가 r번째 열에서 수확을 시작하는 좌표 ej가 열에서 수확을 종료하는 좌표

    print(f"#{tc} {crops}")