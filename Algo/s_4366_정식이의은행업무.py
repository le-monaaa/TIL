import sys
sys.stdin = open("../4366.txt", "r")

# 14 40 50

# SWEA 4366 정식이의 은행업무
# 정식이는 한 숫자를 2진수와 3진수로 기억한다. 컴퓨터인가? 그런데 또 각각 한 글자씩만 잘못 기억하는 걸 보니 그냥 허세다
# 정식이가 잘못 기억하는 송금액을 추측하는 프로그램
# T/ 2진수/3진수

# 2진수 -> 10진수 변환 함수
def binToHex(bin_num):
    bin_num = list(map(int, bin_num))
    num = 1
    sum_n = 0
    for d in bin_num[::-1]:
        sum_n += d * num
        num *= 2
    return sum_n

# 3진수 -> 10진수 변환 함수
def terToHex(ter_num):
    ter_num = list(map(int, ter_num))
    num = 1
    sum_n = 0
    for d in ter_num[::-1]:
        sum_n += d * num
        num *= 3
    return sum_n

T = int(input())
for tc in range(1, T+1):
    bin_n = list(input())
    ter_n = list(input())

    # 2진수 숫자 하나씩을 바꾸면서
    # 3진수 숫자 하나 바꾼 것과 비교
    answer = 0
    for i in range(len(bin_n)):
        if bin_n[i] == "0":
            bin_n[i] = "1"
            temp = binToHex(bin_n)
            for j in range(len(ter_n)):
                for k in ["0", "1", "2"]:
                    t = ter_n[j]
                    if ter_n[j] != k:
                        ter_n[j] = k
                        if temp == terToHex(ter_n):
                            answer = temp
                            break
                    ter_n[j] = t
            bin_n[i] = "0"
            if answer != 0:
                break
        elif bin_n[i] == "1":
            bin_n[i] = "0"
            temp = binToHex(bin_n)
            for j in range(len(ter_n)):
                for k in ["0", "1", "2"]:
                    t = ter_n[j]
                    if ter_n[j] != k:
                        ter_n[j]= k
                        if temp == terToHex(ter_n):
                            answer = temp
                            break
                    ter_n[j] = t
            bin_n[i] = "1"
            if answer != 0:
                break

    print(f"#{tc} {answer}")