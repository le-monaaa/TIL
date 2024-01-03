# SWEA 16530 forth
# 후위표기법을 사용하는 프로그램에 값을 넣었을 때의 출력값 구하기
# 연산 불가일 경우 error 출력
# T/code(여백으로구분됨, 코드는 .로 끝남, 나눗셈은 항상 나누어 떨어진다)

import sys; sys.stdin = open("sample_input(1).txt", "r")

def post(postfix):
    # 후위표기식에서 글자 하나씩 가져오기
    for c in postfix:
        # 피연산자 만나면 스택에 넣기
        if c not in "(*_+/)":
            stack.append(int(c))

        # 연산자를 만나면 스택에서 연산에 필요한 만큼 꺼내서 계산
        # 계산한 결과를 다음 연산에 쓰기 위해서 push
        else:
            if len(stack) < 2: # 연산해야하는데 stack에 피연산자가 부족할 때
                return "error"
            #   연산을 위한 연산자 꺼내기
            b = stack.pop()
            a = stack.pop()
            # 연산
            if c == "+":
                result = a + b
            elif c == "-":
                result = a - b
            elif c == "/":
                result = a / b
            elif c == "*":
                result = a * b
            stack.append(result)
    # 마지막에 남은 결과 하나 꺼내서 확인.
    return stack.pop()

T = int(input())
for tc in range(1, T+1):
    postfix = list(input().split())

    stack = []
    postfix.pop()

    print(f"#{tc} {post(postfix)}")