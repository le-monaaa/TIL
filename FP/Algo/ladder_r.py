T = 10
N = 100
for tc in range(1, T+1):
    int(input()) # 테스트 케이스 번호 입력 처리. 저장, 사용은x

    ladder = [list(map(int, input().split())) for _ in range(N)]

    # 내가 위치를 직접 움직여야 함
    # 행 번호
    r = 99
    # 열 번호
    c = -1 # 마지막행(99)를 검사해서 2인 곳 찾기.
    # 2라고 표시된 곳을 마지막 곳에서 찾기
    for k in range(N):
        if ladder[r][k] == 2:
            c = k

    # 우리가 거슬러 올라갈 위치를 찾았다.
    # 탐색할때 거슬리니까 왔던 길을 0으로 만들어버리면 탐색 시에 돌아가는 일x 사다리를 다 부수면서 올라가는...미로찾기때도이용
    #
    dr = [0, 0, -1] # 좌 우 상
    dc = [-1, 1, 0]

    # 행 번호가 0보다 크면 아직 시작점이 아니니까 계속 이동
    while r > 0:
        # 이동할 때마다 좌-> 우-> 상 순서로 탐색
        for d in range(3):
            # 다음 위치 계산
            nr = r + dr[d]
            nc = c + dc[d]
            # 다음 위치가 유효한 인덱스인지 검사
            if 0 <= nr < N and 0 <= nc < N and ladder[nr][nc] == 1:
                # 갈 수 있으면 간다.
                # 현재 위치 최신화
                r = nr
                c = nc
                # 내가 왔던 길은 다시 보지 않도록 0으로 바꾼다.
                ladder[nr][nc] = 0
                # 길을 찾았으니 다른 방향 볼필요 X
                break

    # 반복문이 끝나면 r이 0이 되었을거니까 출력
    print(f"#{tc} {nc}")


