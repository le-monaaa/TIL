# SWEA 16786 이진수
# 16진수 1자리 -> 2진수 4자리
# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표현하는 프로그램
# 2진수의 앞자리 0도 반드시 출력
# 47FE -> 0100 0111 1111 1110
# T/N/N자리 16진수
import sys
sys.stdin = open("../16786.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, hex = input().split() # n: 16진수의 자릿수, hex: 16진수

    answer = []
    num = 1
    # 10진수로 변환
    print(f"#{tc}", end = " ")
    for d in hex:
        binary = []
        if d not in "ABCDEF": # 숫자인 경우
            for k in range(4):
                d = int(d)
                binary.append(str(d % 2))
                d = d // 2
            print("".join(binary[::-1]),end="")
        else:
            d = int(d, 16)
            for k in range(4):
                binary.append(str(d % 2))
                d = d // 2
            print("".join(binary[::-1]),end ="")
    print()