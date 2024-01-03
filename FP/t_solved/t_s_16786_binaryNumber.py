T = int(input())

for tc in range(1, T + 1):
    n, hex_num = input().split()

    n = int(n)

    # hex_num 를 2진수로 바꾼 결과 문자열
    hex_to_bin = ""

    for i in range(n):
        # i번째 16진수 문자열을 하나씩 떼온다.

        # i번째 16진수 문자열을 2진수로 바꿔서
        # hex_to_bin 에 더해주면 된다.

        # i번째 16진수 문자열을 숫자로 바꾼다.
        ith_num = int(hex_num[i], 16)


        # j번째 문자열 이 1인지 아닌지 검사
        for j in range(3, -1, -1):
            if ith_num & (1 << j) == 0:
                hex_to_bin += "0"
            else:
                hex_to_bin += "1"

    print(f"#{tc} {hex_to_bin}")