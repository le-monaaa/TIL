# SWEA 2005 파스칼의 삼각형
# 크기가 N인 파스칼의 삼각형. 첫번째 줄은 1. 두번째 줄부터는 왼+오 합.
# testcase/ N

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    table = [([0]*n) for _ in range(n)]

    table[0][0] = 1 # 시작점은 무조건 1

    # col = 1은 모두 1
    for r in range(n):
        table[r][0] = 1

    # (i,i) 도 모두 1
    for i in range(n):
        table[i][i] = 1

    # 중간값 채워주기
    for r in range(2, n):
        for c in range(1, n-1):
            if r == c:
                pass
            else:
                table[r][c] = table[r-1][c-1] + table[r-1][c]

    print(f"#{tc}")

    for r in range(n):
        for c in range(n):
            if table[r][c] != 0:
                print(table[r][c], end=" ")
        print()