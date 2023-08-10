# 8*8 테이블. 주어진 길이에 맞는 회문 갯수 찾기
# testcase:10// 찾아야하는 회문의 길이/ 8*8 테이블 내용 주어짐
import sys
sys.stdin = open("input (11).txt", "r")
for tc in range(1, 11):
    n = int(input()) # 회문의 길이
    table = [list(input()) for _ in range(8)]

    cnt = 0
    # 행 순회
    for i in range(8):
        for j in range(8-n+1):
            result = 1
            for k in range(n//2): # 회문인지 체크
                if table[i][j+k] == table[i][j+n-k-1]: # 맞을경우 result값 일정
                    result = 1
                else:
                    result = 0
                    break
            if result == 1: # 끝까지 회문이었을 경우에
                cnt += 1 # 회문 개수 추가

    # 열 순회
    for j in range(8-n+1):
        for i in range(8):
            result = 1
            for k in range(n//2): # 회문인지 체크
                if table[j+k][i] == table[j+n-k-1][i]:
                    result = 1
                else:
                    result = 0
                    break
            if result == 1:
                cnt += 1

    print(f"#{tc} {cnt}")