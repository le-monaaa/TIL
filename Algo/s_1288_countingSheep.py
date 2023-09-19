import sys
sys.stdin = open("../1288.txt", "r")

# SWEA 1288 새로운 불면증 치료법
# n 배수인 양을 세는데. 각 자리수에서 0~9의 모든 숫자를 보는 것은 최소 몇 번 일까?
# T/N

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num = 1
    visited = [0] * 10

    while 0 in visited:
        sn = n * num
        for d in str(sn):
            visited[int(d)] = 1
            if 0 not in visited:
                break
        num += 1

    print(f"#{tc} {sn}")
