import sys
sys.stdin = open('input.txt')



# 팰린들롬 확인 함수 작성
def is_palindrome(string):
    s_len = len(string)

    for idx in range(s_len//2 + 1):
        if string[idx] != string[s_len-1 - idx]:   # 앞과 뒤를 체크
            return False
    return True


T = 10
for tc in range(1, T+1):
    N = 8
    P = int(input())  # 찾는 문자열 개수
    str_arr = [input() for _ in range(N)]

    count = 0
    for line in range(N):               # 행, 열로 체크하기 위한 부분
        for idx in range(N - P + 1):    # 뽑으려는 P 만큼 글자를 뽑기 위한 개수 N - P + 1
            row_str = ''                # 행의 글자
            col_str = ''                # 열의 글자
            for delta in range(P):
                row_str += str_arr[line][idx+delta]
                col_str += str_arr[idx+delta][line]
            # print(row_str, col_str)
            if is_palindrome(row_str):
                count += 1
            if is_palindrome(col_str):
                count += 1
    print(f'#{tc} {count}')
