# SWEA 16638 회전
# N개의 숫자로 이루어진 수열. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때
# 수열의 맨 앞에 있는 숫자를 출력
# T/N(숫자수), M(작업횟수)/N values
import sys
sys.stdin = open("../si1.txt", "r")


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) # n: 숫자 수 m: 작업 횟수
    nums = list(map(int, input().split()))
    size = n
    q = [0] * size

    for i in range(n):
        q[i] = nums[i]

    front = -1
    rear = n-1

    for i in range(m):
        front =
        temp = q[front]

        rear = (rear + 1) % size
        q[rear] = temp


    print(f"#{tc} {q[front +1]}")




