# di = [0, 1, 1, 1]
# dj = [1, 1, 0, -1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     # 입력
#     # N : 배열의 한변의 길이
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#
#     # 로직
#     # 오목이 완성되었는지 여부
#     flag = False
#
#     # 모든 좌표 (i, j)에 대해 순회
#     for i in range(N):
#         for j in range(N):
#             # 델타탐색
#             for k in range(4):
#                 cnt = 0  # 임시 카운트 변수
#                 # 5칸 범위 순회
#                 for mul in range(5):
#                     ni, nj = i + (di[k] * mul), j + (dj[k] * mul)
#                     if 0 <= ni < N and 0 <= nj < N:
#                         # 돌이 놓여져 있는가...
#                         if arr[ni][nj] == 'o':
#                             cnt += 1
#                 if cnt == 5:  # 오목이 완성된 경우이기 때문에
#                     flag = True  # 오목 성공..
#
#     # 출력
#     if flag == True:  # 오목이 있다면
#         print(f"#{tc} YES")
#     else:
#         print(f"#{tc} NO")


# di = [0, 1, 1, 1]
# dj = [1, 1, 0, -1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     # 입력
#     # N : 배열의 한변의 길이
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#
#     # 로직
#     # 오목이 완성되었는지 여부
#     flag = False
#
#     # 모든 좌표 (i, j)에 대해 순회
#     for i in range(N):
#         for j in range(N):
#             # 델타탐색
#             for k in range(4):
#                 cnt = 0  # 임시 카운트 변수
#                 # 5칸 범위 순회
#                 for mul in range(5):
#                     ni, nj = i + (di[k] * mul), j + (dj[k] * mul)
#                     if 0 <= ni < N and 0 <= nj < N:
#                         # 돌이 놓여져 있는가...
#                         if arr[ni][nj] == 'o':
#                             cnt += 1
#                 if cnt == 5:  # 오목이 완성된 경우이기 때문에
#                     flag = True  # 오목 성공..
#                     break
#             if flag == True:
#                 break
#         if flag == True:
#             break
#
#     # 출력
#     if flag == True:  # 오목이 있다면
#         print(f"#{tc} YES")
#     else:
#         print(f"#{tc} NO")


# di = [0, 1, 1, 1]
# dj = [1, 1, 0, -1]
#
# T = int(input())
#
#
# def solution():
#     # 모든 좌표 (i, j)에 대해 순회
#     for i in range(N):
#         for j in range(N):
#             # 델타탐색
#             for k in range(4):
#                 cnt = 0  # 임시 카운트 변수
#                 # 5칸 범위 순회
#                 for mul in range(5):
#                     ni, nj = i + (di[k] * mul), j + (dj[k] * mul)
#                     if 0 <= ni < N and 0 <= nj < N:
#                         # 돌이 놓여져 있는가...
#                         if arr[ni][nj] == 'o':
#                             cnt += 1
#                 if cnt == 5:  # 오목이 완성된 경우이기 때문에
#                     return True  # 오목 성공..
#     # 오목이 없는 경우는 실패...
#     return False
#
#
# for tc in range(1, T + 1):
#     # 입력
#     # N : 배열의 한변의 길이
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#
#     # 로직
#     # 오목이 완성되었는지 여부
#     answer = solution()
#
#     # 출력
#     if answer == True:  # 오목이 있다면
#         print(f"#{tc} YES")
#     else:
#         print(f"#{tc} NO")


di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]

T = int(input())


def solution(N, arr):
    # 모든 좌표 (i, j)에 대해 순회
    for i in range(N):
        for j in range(N):
            # 델타탐색
            for k in range(4):
                cnt = 0  # 임시 카운트 변수
                # 5칸 범위 순회
                for mul in range(5):
                    ni, nj = i + (di[k] * mul), j + (dj[k] * mul)
                    if 0 <= ni < N and 0 <= nj < N:
                        # 돌이 놓여져 있는가...
                        if arr[ni][nj] == 'o':
                            cnt += 1
                if cnt == 5:  # 오목이 완성된 경우이기 때문에
                    return True  # 오목 성공..
    # 오목이 없는 경우는 실패...
    return False


for tc in range(1, T + 1):
    # 입력
    # N : 배열의 한변의 길이
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 로직
    # 오목이 완성되었는지 여부
    answer = solution(N, arr)

    # 출력
    if answer == True:  # 오목이 있다면
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")