# baekjoon 스택
# push, pop, size, empty, top 을 수행하여 결과를 출력
# N/command

import sys
input=sys.stdin.readline

N = int(input()) # N: 명령어 수
stack = []
for n in range(N):
    full_command = input()
    if full_command[:4] == "push":
        a, b = full_command.split()
        stack.append(b)
    elif full_command[:3] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif full_command[:4] == "size":
        print(len(stack))
    elif full_command[:3] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            a = stack.pop()
            print(a)
            stack.append(a)
    else: # empty
        if len(stack) == 0:
            print(1)
        else:
            print(0)
