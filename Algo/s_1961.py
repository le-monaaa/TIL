# SWEA 1961 숫자 배열 회전
# N*N 행렬. 90도, 180도, 270도 회전한 모양 출력
# T/N/N*N 행렬

# def rote(n, arr):
#     table1 = [] for _ in range(n):
#         print(table1)



T = int(input())
for tc in range(1, 2):
    N = int(input())
    table = [list(map(int, input().split())) for _  in range(N)]
    print(table)
