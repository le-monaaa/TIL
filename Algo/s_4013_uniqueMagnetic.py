import sys;sys.stdin = open("../4013.txt", "r")

# SWEA 4013 특이한 자석
# 4개의 자석 일렬배치. 8개짜리 톱니 모양. 8군데에 N or S극 존재. 1, 2, 3, 4 순서로 배치
# 임의의 자석을 1칸씩 k번 회전-> 붙어 있는 자석은 서로 접촉한 톱니의 자성과 다를 경우에만 반대방향으로 1 회전
# 그니까 체크해서 같은 극이면 안돌아간다. 다른 극이면 반대 톱니가 반대로 한 칸 회전.
# 모든 회전 후 1,2,3,4 자석의 첨단이 S극일 때 각각 1,2,4,8 점 획득. 점수를 출력
# T/ K/ 4 lines 8 values/ K spin infos

# 회전 여부 판단
def check1(work_mag, spin_info):
    work[0] = spin_info
    # 1번이 돌아가는 주체일 때
    if work_mag == 1:
        # 2번과 닿은 부분이 같은 극
        if magnetics[0][2] != magnetics[1][-2]:
            check2(work_mag, spin_info * (-1))


def check2(work_mag, spin_info):
    work[1] = spin_info
    # 2번이 돌아가는 주체이다
    if work_mag == 2:
        # 1번과 닿은 부분이 같은 극이 아닐 때
        if magnetics[0][2] != magnetics[1][-2]:
            check1(work_mag, spin_info*(-1))
        # 3번과 닿은 부분이 같은 극이 아닐 때
        if magnetics[1][2] != magnetics[2][-2]:
            check3(work_mag, spin_info*(-1))
    # 2번이 돌아가는 주체가 아니다
    else:
        if work_mag != 1 and work[0] == 0:
            if magnetics[0][2] != magnetics[1][-2]:
                check1(work_mag, spin_info*(-1))
        if work_mag != 3 and work[2] == 0:
            if magnetics[1][2] != magnetics[2][-2]:
                check3(work_mag, spin_info*(-1))

def check3(work_mag, spin_info):
    work[2] = spin_info
    if work_mag == 3:
        # 2번과 닿은 부분이 다른 극일 때
        if magnetics[1][2] != magnetics[2][-2]:
            check2(work_mag, spin_info * (-1))
        # 4번과 닿은 부분이 다른 극일 때
        if magnetics[2][2] != magnetics[3][-2]:
            check4(work_mag, spin_info * (-1))
    else:
        if work_mag != 2 and work[1] == 0:
            if magnetics[1][2] != magnetics[2][-2]:
                check2(work_mag, spin_info * (-1))
        if work_mag != 4 and work[3] == 0:
            if magnetics[2][2] != magnetics[3][-2]:
                check4(work_mag, spin_info * (-1))


def check4(work_mag, spin_info):
    work[3] = spin_info
    # 4번이 돌아가는 주체일 때
    if work_mag == 4:
        if magnetics[2][2] != magnetics[3][-2]:
            check3(work_mag, spin_info * (-1))


T = int(input())
for tc in range(1, T+1):
    k = int(input()) # k: 회전 횟수
    magnetics = [list(map(int, input().split())) for _ in range(4)]

    # 회전 정보를 하나씩 받아서 작업함..
    for K in range(k):
        mag, spin = map(int, input().split())

        work = [0] * 4

        if mag == 1:
            check1(mag, spin)
        elif mag == 2:
            check2(mag, spin)
        elif mag == 3:
            check3(mag, spin)
        else:
            check4(mag, spin)
        idx = 0
        # 회전
        for i in work:
            # 정방향 회전일 때
            if i == 1:
                magnetics[idx].insert(0, magnetics[idx].pop())
            # 역방향 회전일 때
            elif i == -1:
                magnetics[idx].append(magnetics[idx].pop(0))
            else:
                pass
            idx += 1

    # 점수 연산/ N = 0 S =1
    idx = 0
    score = 0
    num = 1
    for i in range(4):
        if magnetics[idx][0] == 1:
            score += num
        idx += 1
        num *= 2

    print(f"#{tc} {score}")


