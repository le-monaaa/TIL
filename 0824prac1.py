pat = {
    "001101": 0,
    "010011": 1,
    "111011": 2,
    "110001": 3,
    "100011": 4,
    "110111": 5,
    "001011": 6,
    "111101": 7,
    "011001": 8,
    "101111": 9,
}
"000000"

hex1 = "0DEC"
hex2 = "0269FAC9A0"


def find_pattern(hex_string):
    # hex_string 은 16진수 문자열
    # 이진수 문자열로 바꾸면 길이가 4배
    l = len(hex_string) * 4
    x = int(hex_string, 16)  # 숫자로 바꾸기

    # 숫자를 다시 이진수 문자열로 바꾸기
    bin_string = ""

    # i번째 비트를 검사 해서 결과가 0 => i번째 비트는 0
    # 결과가 0이 아니면 i번째 비트는 1
    for i in range(l - 1, -1, -1):
        bin_string += "1" if x & (1 << i) else "0"

    bin_list = list(bin_string)  # 가변 타입 리스트로 바꾸기

    result = ""
    # 뒤에서부터 검사 해서 1을 만나면 암호 해독 시작
    # 1을 만난 순간부터 6개씩 잘라서 검사
    for i in range(l - 1, 5, -1):
        # 1을 만난 순간부터 6개씩 잘라서 검사
        if bin_list[i] == "0":
            continue

        # 1을 만났다.
        code = "".join(bin_list[i - 5:i + 1])

        # 6개 잘라온 코드가 암호 표에 있는지 검사
        dec = pat.get(code)

        if dec != None:
            result += str(dec) + ","

            # 암호코드 변경한 나머지 5칸에서 패턴을 또 찾지 않도록 처리
            for j in range(i, i - 6, -1):
                bin_list[j] = "0"

    print(result[::-1])


find_pattern(hex1)
find_pattern(hex2)
