T = int(input())

for tc in range(1, T+1):
    n = int(input()) #색칠 횟수

    paper = [[0] * 10 for _ in range(10)] # 10*10 종이 생성

    purple_count = 0 #보라색 칸 갯수

    # n번 반복하면서 색칠하는데 겹친 칸 갯수 세기
    for i in range(n):
        sr, sc, er, ec, color = map(int, input().split())

        # 색칠 범위
        # 색칠 시작 행 ~ 색칠 끝 행
        for r in range(sr, er+1):
            #색칠 시작 열 ~ 색칠 끝 열
            for c in range(sc, ec + 1):
                # 색칠하기 전 다른 색이 있다면 보라색이 됨
                if paper[r][c] == 0:
                    paper[r][c] = color
                else:
                    # 0이 아니면 다른 색이 칠해져 있다
                    purple_count += 1

    print(f"#{tc} {purple_count}")