# SWEA 1234 비밀번호
# 0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍을 소거하고 남은 번호 출력
# 10/n:문자열 길이/num: 문자열
import sys
sys.stdin = open("../i1.txt", "r")

for tc in range(1, 11):
    n, num = input().split()
    num = list(num)

    i = 0
    while i < len(num)-1:
        if num[i] == num[i+1]:
            del num[i:i+2]
            i = 0
        else:
            i += 1

    result = "".join(num).split()
    print(f"#{tc}", end=" ")
    print(*result)

