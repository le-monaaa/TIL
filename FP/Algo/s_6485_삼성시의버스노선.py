# SWEA 6485 삼성시의 버스 노선
# 1~5000 정류장.
# T/N/A,B/P/P lines J, C

T = int(input())
for tc in range(1, T+1):
    stop = [0]* 5001
    n = int(input()) # n: 버스 노선의 개수

    for i in range(n):
        a, b = map(int, input().split())  # 번호가 a이상이고 b이하인 모든 정류장을 다니는 버스
        for k in range(a, b+1):
            stop[k] += 1
    print(f"#{tc}", end = " ")
    p = int(input()) # p개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지.
    for i in range(p):
        c = int(input())
        print(f"{stop[c]}", end = " ")
    print()