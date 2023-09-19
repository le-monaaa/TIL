"""
10
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
"""
# # 테스트케이스
# T = int(input())
# for tc in range(1, T + 1):
#     # 입력
#     # 퍼즐의 길이 N, 특정 문자 길이 K
#     N, K = map(int, input().split())
#     # 퍼즐 N * N
#     puzzle = [list(map(int, input().split())) for _ in range(N)]
#
#
#     # 로직
#
#     ans = 0
#     cnt = 0
#     # 퍼즐을 행 우선 순회
#     for i in range(N):
#         for j in range(N):
#             # 빈칸을 만나게 되면 cnt += 1
#             if puzzle[i][j] == 1: # 빈칸이라면
#                 cnt += 1
#             # 벽이라면 또는 배열 끝
#             if puzzle[i][j] == 0 or j == N - 1:
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#
#     # 퍼즐을 행 우선 순회
#     for j in range(N):
#         for i in range(N):
#             # 빈칸을 만나게 되면 cnt += 1
#             if puzzle[i][j] == 1: # 빈칸이라면
#                 cnt += 1
#             # 벽이라면 또는 배열 끝
#             if puzzle[i][j] == 0 or i == N - 1:
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#
#
#     # 출력
#     print(f"#{tc} {ans}")

# 테스트케이스
# T = int(input())
# for tc in range(1, T + 1):
#     # 입력
#     # 퍼즐의 길이 N, 특정 문자 길이 K
#     N, K = map(int, input().split())
#     # 퍼즐 N * N
#     puzzle = [list(map(int, input().split())) for _ in range(N)]
#     # 퍼즐's 전치행렬 (행 <-> 열)
#     puzzle_t = [list(i) for i in zip(*puzzle)]
#
#     # 로직
#
#     ans = 0
#     cnt = 0
#     # 퍼즐을 행 우선 순회
#     for i in range(N):
#         for j in range(N):
#             # 빈칸을 만나게 되면 cnt += 1
#             if puzzle[i][j] == 1: # 빈칸이라면
#                 cnt += 1
#             # 벽이라면 또는 배열 끝
#             if puzzle[i][j] == 0 or j == N - 1:
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#
#     # 전치행렬을 기준으로 행 우선 순회
#     for i in range(N):
#         for j in range(N):
#             # 빈칸을 만나게 되면 cnt += 1
#             if puzzle_t[i][j] == 1: # 빈칸이라면
#                 cnt += 1
#             # 벽이라면 또는 배열 끝
#             if puzzle_t[i][j] == 0 or j == N - 1:
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#
#     # 출력
#     print(f"#{tc} {ans}")

T = int(input())


def count(arr):
    result = 0
    cnt = 0
    # 퍼즐을 행 우선 순회
    for i in range(N):
        for j in range(N):
            # 빈칸을 만나게 되면 cnt += 1
            if arr[i][j] == 1:  # 빈칸이라면
                cnt += 1
            # 벽이라면 또는 배열 끝
            if arr[i][j] == 0 or j == N - 1:
                if cnt == K:
                    result += 1
                cnt = 0
    return result


for tc in range(1, T + 1):
    # 입력
    # 퍼즐의 길이 N, 특정 문자 길이 K
    N, K = map(int, input().split())
    # 퍼즐 N * N
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 퍼즐's 전치행렬 (행 <-> 열)
    puzzle_t = [list(i) for i in zip(*puzzle)]

    # 로직
    ans = count(puzzle) + count(puzzle_t)
    # 출력
    print(f"#{tc} {ans}")