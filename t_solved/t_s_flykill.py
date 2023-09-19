# 상하좌우 (델타값)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 대각선 (델타값)
di_x = [-1, -1, 1, 1]
dj_x = [-1, 1, -1, 1]

# 테스트케이스 수
T = int(input())

for tc in range(1, T + 1):
    # 입력
    # N : 배열의 한변의 길이, M : 스프레이를 뿌리는 범위
    N, M = map(int, input().split())
    # arr : N * N 짜리의 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 로직

    # 가장 최대로 많이 죽인 파리 수
    mx = 0

    # 모든 좌표 순회 (i, j)
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]  # 합산을 진행할 임시 카운트 변수
            # 사방탐색 (상하좌우)
            for k in range(4):
                # M 만큼 범위를 늘려서 탐색
                for mul in range(1, M):
                    ni, nj = i + (di[k] * mul), j + (dj[k] * mul)
                    # 범위 바깥으로 나갔지도 확인
                    if 0 <= ni < N and 0 <= nj < N:
                        # 합산
                        cnt += arr[ni][nj]
            # 가장 파리를 많이 죽인 값으로 갱신...
            mx = max(mx, cnt)

    # 모든 좌표 순회 (i, j)
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]  # 합산을 진행할 임시 카운트 변수
            # 사방탐색 (상하좌우)
            for k in range(4):
                # M 만큼 범위를 늘려서 탐색
                for mul in range(1, M):
                    ni, nj = i + (di_x[k] * mul), j + (di_x[k] * mul)
                    # 범위 바깥으로 나갔지도 확인
                    if 0 <= ni < N and 0 <= nj < N:
                        # 합산
                        cnt += arr[ni][nj]
            # 가장 파리를 많이 죽인 값으로 갱신...
            mx = max(mx, cnt)

    # 출력
    print(f"#{tc} {mx}")