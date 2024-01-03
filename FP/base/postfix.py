# 스택 밖에 있을 때 우선 순위
icp = {"+": 1, "-": 1, "/": 2, "*": 2, "(": 3}
# 스택 안에 있을 때 우선 순위
isp = {"+": 1, "-": 1, "/": 2, "*": 2, "(": 0}


# 중위표기식을 후위표기식으로 바꾸기
# infix // postfix

# infix : 후위표기식으로 바꿀 중위표기식
# n : 식의 길이
def get_postfix(infix, n):
    postfix = ""  # 결과로 출력할 후위 표기식
    stack = []

    # 문자열(중위표기식)에서 글자 하나씩 떼오기
    for i in range(n):
        # i 번째 글자가 피연산자인지
        if infix[i] not in "(+-/*)":
            # 결과에 출력
            postfix += infix[i]

        # i 번째 글자가 연산자인지
        else:
            # 닫는 괄호가 나오는 경우
            if infix[i] == ")":
                # 여는 괄호가 나올때 까지 pop해서 결과 출력
                while stack:
                    temp = stack.pop()
                    if temp == "(":
                        break
                    postfix += temp
            # 닫는 괄호가 아닌 다른 연산자가 나오는 경우
            else:
                # 현재 토큰(연산자)의 우선순위보다
                # stack[top]에 있는 연산자의 우선순위가 같거나 높으면
                # 계속 pop 해서 출력
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                # 그게아니면 push()
                stack.append(infix[i])

    # 남아있는 연산자들 출력
    while stack:
        postfix += stack.pop()

    return postfix


# 2. 후위표기식의 결과를 계산할 함수
def get_result(postfix):
    stack = []

    # 후위표기식에서 글자 하나씩 떼오기
    for c in postfix:

        # 피연산자를 만나면 스택에 넣기
        if c not in "(+-/*)":
            stack.append(int(c))  # 타입 조심

        # 연산자를 만나면 스택에서 연산에 필요한 만큼 꺼내서 계산
        # 계산한 결과를 다음연산에 쓰기위해서 push
        else:
            # 오른쪽이 먼저
            right = stack.pop()
            # 왼쪽이 나중에
            left = stack.pop()

            # 연산자의 종류에 따라서 계산
            if c == "+":
                result = left + right
            if c == "-":
                result = left - right
            if c == "/":
                result = left / right
            if c == "*":
                result = left * right

            # 계산 결과를 다음 연산자에서 쓰기 위해
            # 여기의 계산 결과가 다음 연산자의 피연산자가 됨
            stack.append(result)

    # 마지막에 남은 결과 하나 꺼내서 확인
    return stack.pop()


string = "2+3*4/5"
n = len(string)
postfix = get_postfix(string, n)
print(postfix)

print(get_result(postfix))