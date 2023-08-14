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

    # 막대 수 = 전체 막대 갯수 + 레이저 만난 횟수

    pipe = 0 # 활성화 막대 수
    laser = 0 # 레이저 만난 횟수
    pipes = 0 # 전체 막대 개수

    for i in range(len(line)):
        if line[i] == "(": # "("를 만나면 전체 막대 개수++ 현재 막대 개수++
            pipes += 1
            pipe += 1
        elif line[i] == ")": # ")"를 만나면 막대개수-- 카운트+1
            pipe -= 1
        elif line[i] == "L": # "L"을 만나면 자르기(현재 막대수*2)
            laser = laser + pipe
    result = laser + pipes
    print(f"#{tc} {result}")
