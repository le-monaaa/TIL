# baekjoon 9012 괄호
# () VPS 검사.
# T/ testcases

# import sys
# sys.stdin = open("testcase.txt", "r")

T = int(input())
for tc in range(T):
    stack = []
    testcase = list(input())

    while testcase:
        item = testcase.pop(0)
        if item == "(":
            stack.append(item)
        else: # item == ")"
            if len(stack) == 0:
                testcase.append(item)
                break
            else:
                stack.pop()

    if len(testcase) == 0 and len(stack) ==0:
        print("YES")
    else:
        print("NO")