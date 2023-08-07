# N*N 크기의 단어 퍼즐. 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는
# 특정 길이 K를 갖는 단어의 수 출력
#

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0 #단어가 들어갈수 있는 자리의 수
    for i in range(N): # 행 우선 순회
        cnt = 0         #연속한 빈칸의 수
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            if j == N-1 or arr[i][j] ==0:
                if cnt==K:
                    ans  += 1
                cnt = 0
        print(ans)