# SWEA 1989 초심자의 회문 검사
# testcase/ word

T = int(input())
for tc in range(1, T+1):
    word = input()
    result = 0
    if word == "".join(list(word)[::-1]):
        result = 1
    print(f"#{tc} {result}")