# 16진수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오.

pat = { "001101" : 0,
        "010011" : 1,
        "111011" : 2,
        "110001" : 3,
        "100011" : 4,
        "110111" : 5,
        "001011" : 6,
        "111101" : 7,
        "011001" : 8,
        "101111" : 9
        }

def find_pattern(hex_string):
    # hex_string은 16진수 문자열
    # 2진수 문자열로 바꾸면 길이가 4배
    l = len(hex_string) * 4
    # 16진수 숫자로 바꾸기
    x = int(hex_string, 16)

    # 숫자를 다시 이진수 문자열로 바꾸기
    bin_String = ""

    # i번째 비트를 검사해서 결과가 0이면 i번째 비트는 0
    # 0이 아니면 1
    for i in range(l-1, -1, -1):
        if x & (1<<i) == 1:
            bin_String += "1"
        else:
            bin_String += "0"
    bin_list = list(bin_String)
    result = ""
    # 뒤에서부터 검사해서 1을 만나면 암호 해독 시작
    # 1을 만난 순간부터 6개씩 잘라서 검사
    for i in range(l, -5, -1):
        if bin_String[i] == "0":
            continue
        # 1을 만나면
        code = "".join(bin_String[i - 5 : i + 1])

        # 6개 잘라온 코드가 암호 표에 있는지 검사
        dec = pat.get(code)

        if dec != None:
            result += str(dec)




