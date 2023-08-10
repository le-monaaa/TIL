# SWEA 16478 반복문자 지우기
# 문자열 s에서 반복된 문자를 지운다. 지워진 부분은 연결, 다시 반복문자되면 또 삭제
# 지운 후 남은 문자열의 크기. 없으면 0 출력
# testcase/ line
import sys
sys.stdin = open("../si1.txt", "r")
'''
T = int(input())
for tc in range(1, T+1):
    line = list(input())
    i = 1
    while -1 < i < len(line): #범위 내일 경우에만.
        if line[i-1] == line[i]:
            if i - 1 < 0:
                break
            else:
                del line[i-1: i+1]
                i = 1
        else:
            i += 1
    if len(line) == 2 and line[0] == line[1]:
        line = ""

    result = len("".join(line))

    print(f"#{tc} {result}")
'''
### 스택으로 풀기
T = int(input())
for tc in range(1, T+1):
    text = input()
    size = 1000 # 문자열 최대 길이가 1000이라 함.
    stack = [0] * size
    top = -1 # 마지막으로 삽입한 원소의 위치
    # 첫 번째 문자를 스택에 넣음
    top += 1
    stack[top] = text[0]

    # 두 번째 글자부터는 내가 제일 마지막에 넣었던 글자와 비교해서
    for i in range(1, len(text)):
        # 같으면 스택에서 pop
        if top != -1:
            if stack[top] == text[i]:
                top -= 1
            # 다르면 현재 글자를 스택에 push
            else:
                top += 1
                stack[top] = text[i]

    # 마지막으로 원소가 삽입된 위치가 top이니까 길이는 top +1
    print(f"#{tc} {top + 1}")
    # 뭐지 답이 다른데
