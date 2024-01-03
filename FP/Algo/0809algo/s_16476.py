# SWEA 16476 괄호검사
# 괄호가 짝이 맞는지 검사 {} () . 정상적으로 짝을 이루면 1, 아니면 0
# testcase/code
import sys
sys.stdin = open("../input1 (2).txt", "r")

T = int(input())
for tc in range(1, T+1):
    code = input()

    stack = []

    i = 0
    result = 1
    while i < len(code):
        if code[i] == "{" or code[i] == "(": # 여는괄호일 경우
            stack.append(code[i])
        if code[i] == "}" or code[i] == ")": # 닫는괄호일 경우
            if len(stack) != 0: # stack이 빈 배열이 아닐 경우에만 검사
                a = stack.pop()
                if code[i] == "}":  # 닫는괄호 - } 일 경우
                    if a != "{":
                        result = 0
                        break
                elif code[i] == ")":  # 닫는괄호 - ) 일 경우
                    if a != "(":
                        result = 0
                        break
            else: # stack에 든 게 없을 경우
                result = 0
                break
        i += 1
    if len(stack) != 0:
        result = 0


    # result 출력
    print(f"#{tc} {result}")