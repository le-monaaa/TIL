# SWEA 16788 이진수2
# 0<N<1 십진수 N을 이진수로 바꿔 출력
# N 을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자 출력,
# 13자리 이상이 필요하면 overflow를 출력
# T, N(소수점 아래가 12자리 이내)

import sys
sys.stdin = open("../16788.txt", "r")

def change_binary(num):
    binary_num = []
    while num != 0:
        num *= 2
        if num >= 1:
            num -= 1
            binary_num.append("1")
        else:
            binary_num.append("0")

    result = "".join(binary_num)
    if len(result) >= 13:
        result = "overflow"
    return result



T = int(input())
for tc in range(1, T+1):
    n = float(input())

    answer = change_binary(n)

    print(f"#{tc} {answer}")