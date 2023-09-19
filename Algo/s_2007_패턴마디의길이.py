# SWEA 2007 패턴 마디의 길이
# 패턴 길이 상한 10 전체 문자열 길이 30
# T/line
import sys
sys.stdin = open("../2007.txt", "r")

T = int(input())
for tc in range(1, T+1):
    line = input()

    for i in range(10):
        temp = line[:i]
        if temp == line[i:i+len(temp)]:
            pattern = temp

    n = len(pattern)
    if pattern[:len(pattern)//2] == pattern[len(pattern)//2:]:
        pattern = pattern[:len(pattern)//2]
    else:
        while n>2:
            n = n//2
            for i in range(1, n):
                temp = pattern[0:i]
                if temp == pattern[i:i+len(temp)]:
                    pattern = temp

    print(f"#{tc} {len(pattern)}")
