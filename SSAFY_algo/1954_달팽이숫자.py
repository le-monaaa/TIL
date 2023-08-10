# 1부터 N*N까지의 숫자가 시계방향으로.
#### 해결x
T = int(input())
for t in range(1 , T + 1):
    n = int(input())

    table = [[0 for _ in range(n)] for i in range(n)] # N * N의 0으로 초기화된 배열 생성
    row, col, num = 0, 0, 1

    for r in range(n*n): # 행 수 n번만큼 반복
        num += 1
        if row < 1:
            table[row][col] = num
            col += 1
        else:
            if row < 0 or row > n-1 or col < 0 or col > n-1:
                if col > n-1 or table[row][col] != 0: #우측으로 더이상 x -> 아래로
                    col -= 1
                    row += 1
                    table[row][col] = num
                    row += 1
                elif row > n-1 or table[row][col] != 0: # 아래로 더이상 x -> 좌측으로
                    num -= 1
                    row -= 1
                    col -= 1
                    table[row][col] = num
                    col -= 1
                elif col < 0 or table[row][col] != 0: # 좌측으로 더이상 x -> 우측으로
                    # num -= 1
                    col += 1
                    row -= 1
                    table[row][col] = num
                    row -= 1
        print(f"table[{row}][{col}] = {table[row][col]}")