# SWEA 5432 쇠막대기 자르기
# 쇠막대는 자신보다 긴 쇠막대 위에만 놓임. 이경우 완전히 포함되도록 놓되 끝점은 겹치지 않음
# 모든 쇠막대는 적어도 하나 이상의 레이저에 의해 잘림. 레이저는 쇠막대의 끝점과 겹치지 않음
# 왜 이런짓을?
# 레이저는 ()로 표현됨. 쇠막대는 (    ) 로 표현.
# T/테스트케이스~~
import sys
sys.stdin = open("si2.txt", "r")

T = int(input())
for tc in range(1, T+1):
    line = list(input())

    # () 레이저있는 곳 인덱스 하나로 만들기
    for i in range(len(line)-1):
        if line[i] == "(" and line[i+1] == ")":
            line[i] = "L"
            line[i+1] = ""
    line = [i for i in line if i] # 공백제거

    # 레이저 리스트
    laser = []
    for i in range(len(line)):
        if line[i] == "L":
            laser.append(i)

    # 쇠막대 리스트
    pipes = []
    i = 0
    while i < len(line):
        if line[i] == "(": # ( 인덱스값 계속 갱신
            start = i
            # print(f"i = {i}, start = {start}")
            i += 1
        elif line[i] == ")": # ) 만나면 둘다 0으로 바꿔버리고 리스트에 위치 저장
            end = i
            pipes.append(list(i for i in range(start, end)))
            # print(f"i = {i} end = {end}, start = {start}, pipes = {pipes} line = {line}")
            line[start] = 0
            line[end]= 0
            i = 0
        else: # 모두 해당 없을 때
            i += 1
    # print(f"laser = {laser}")

    # 카운팅
    cnt = 0
    for j in range(len(pipes)):
        cnt += 1
        for l in laser:
            if l in pipes[j]:
                cnt += 1
    #
    print(f"#{tc} {cnt}")