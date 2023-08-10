# SWEA 1213 String
# 주어지는 영어 문장 내 특정 문자열의 개수 반환 프로그램
# testcase= 10/tc/특정문자열/검색할문장
import sys
sys.stdin = open("test_input.txt", "rt", encoding="UTF8")

for tc in range(1, 11):
    n = input()
    pt = list(input())
    txt = list(input())
    pl = len(pt)

    i = 0
    cnt = 0
    while i < len(txt):
        if txt[i:i+pl] == pt:
            cnt += 1
            i += pl
        i += 1

    print("#{} {}".format(tc, cnt))

