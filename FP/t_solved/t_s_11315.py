
T = int(input())

# 델타배열
# 4방향만 봐도 됨 쌍방이면 같은거기때문에

dr = [0, 1, 1, 1] # 우 우하 하 좌하
dc = [1, 1, 0, -1]

def is_valid(r,c):
    return 0 <= r < N and 0 <= c < N

def solve():
    # 모든 위치 (r,c)에서 돌("o")을 발견하면
    # 그 돌과 연결된 돌들이 5개 있는지 확인
    # 5개 있으면 "YES"
    # 하나도 발견하지 못하면 "NO"

    for r in range(N):
        for c in range(N):
            # (r,c)에서 돌을 발견 했다
            if arr[r][c] == "o":
                # 4방향으로 탐색(이어진 돌의 개수 세기)
                for d in range(4):
                    # 오목이니까 한방향당 5칸씩 가보기
                    for k in range(5):
                        nr = r + dr[d] * k
                        nc = c + dc[d] * k
                        # 열, 행번호 * 한칸씩 체크가능
                        #다음위치 계산했는데 돌이 아니거나 범위 밖이면 중단
                        if not is_valid(nr, nc) or arr[nr][nc] == ".":
                            # 유효한 위치인지 확인하는 함수//아니면 if로 체크해도됨
                            break
                            # 둘중의 하나만이라도 False 이면 조건불충족
                        else:
                            # 5개를 체크할 동안 모두 True
                            return "YES"
    # 함수가 종료되지 않고 여기까지 실행된 경우
    # 오목을 찾지 못했다.
    return "NO"

for tc in range(1, T+1):
    N = int(input())
    #바둑판
    arr = list(input() for _ in range(N))

    print(f"#{tc} {solve()} ")

