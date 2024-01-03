# SWEA 1232 사칙연산
# + - * / 와 양의 정수로 구성된 이진 트리. 계산한 결과 출력
# tc 10/N/
# N이 정수면 정점 번호, 양의 정수
# N이 연산자면 정점 번호, 연산자, 해당 정점의 왼,오른쪽의 정점 번호
# 정점 번호는 1~N. 루트정점은 1.
import sys
sys.stdin = open("1232.txt", "r")

# 후위순회해서 답 도출
def postorder(t):
    if t:
        postorder(c_left[t])
        postorder(c_right[t])
        post.append(info[t])

T = 10
for tc in range(1, T+1):
    n = int(input()) # 정점의 개수
    info = [0] * (n+1)
    c_left = [0] * (n+1)
    c_right = [0] * (n+1)
    for i in range(n): # 정점 개수 만큼 반복
        temp = list(input().split())
        for c in range(len(temp)):
            if temp[c].isdigit():
                temp[c] = int(temp[c])
        if type(temp[1]) == int: # 정점이 정수인 경우/ 정점 번호, 양의 정수
            info[temp[0]] = temp[1]
        else: # 정점이 연산자인 경우/ 정점 번호, 연산자, 왼쪽 자식 정점 번호, 오른쪽 자식 정점 번호
            info[temp[0]] = temp[1]
            c_left[temp[0]] = temp[2]
            c_right[temp[0]] = temp[3]

    post = []
    postorder(1)
    stack = []

    # 연산하기
    for t in post:
        if type(t) == int: # 정수일 때
            stack.append(t)
        else:
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                result = a + b
                stack.append(result)
            if t == "-":
                result = a - b
                stack.append(result)
            if t == "*":
                result = a * b
                stack.append(result)
            if t == "/":
                result = a // b
                stack.append(result)

    answer = stack.pop()

    print(f"#{tc} {answer}")


