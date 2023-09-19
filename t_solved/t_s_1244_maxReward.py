import sys
sys.stdin = open("1244.txt", "r")

# SWEA 1244 최대 상금
# 주어진 숫자들 중 두개를 정해진 횟수만큼 서로의 자리의 위치를 교환할 수 있음.
# 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 됨
# 교환 후엔 오른쪽부터 왼쪽까지 1부터 10씩 가중되어 상금 계산됨. 최대상금은?
# T/numbers, times

def swap(cnt): # cnt만큼 바꿨다..
    global answer
    # 종료 조건 : 교환 횟수를 다 소모했다면
    # 바꾼 결과물을 숫자로 바꿔서 최대 상금 계산
    if cnt == N:
        answer = max(answer, int("".join(S)))
        return

    # 자리를 바꿀 위치 2개를 교환 한 번 할 때마다 새로 지정해줘야 함
    # 이 문제에서는 동일한 위치에서 중복 교환을 허용
    # i: 바꿀 위치 중 앞쪽 j: 바꿀 위치 중 뒷쪽
    # 이미 처리한 값이면 다시 연산 X (교환횟수랑 int(S))
    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            S[i], S[j] = S[j],S[i]
            temp = int("".join(S))
            #이미 해 본 값이라면 X
            if (cnt, temp) not in visited:
                swap(cnt+1)
                visited.append((cnt, temp))
            # 바꿨던 거 원상복구
            S[i], S[j] = S[j], S[i]

T = int(input())

for tc in range(1, T+1):
    S, N = input().split() # S: 숫자판 N: 시도 횟수

    S = list(S)
    N = int(N)
    answer = 0
    visited = []
    swap(0)

    print(f"#{tc} {answer}")