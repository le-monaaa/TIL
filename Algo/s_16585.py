# SWEA 16585 토너먼트 카드게임
# 1번부터 N번까지 N명의 학생이 N개의 카드를 나눠가짐. 전체를 두 그룹으로 나누고 그룹 내 승자끼리 비교해 이긴 사람이 최종승자
# i번부터 j번까지 속한 그룹은 (i+j)//2 까지와 (i+j)//2+1부터.
# 두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가림. 다시 더 큰 승자를 뽑는~~
# 1 == 가위 2 == 바위 3 == 보. 같은 카드라면 숫자가 작은 쪽이 승리
# N명의 학생들이 카드를 골랐을 때 1등을 찾는 프로그램
import sys
sys.stdin = open("si2.txt", "r")

# 가위바위보 승자를 가려내는 함수
def win(l, r):
    if l == r:
        return l
    if l == 1:
        if r == 2:
            return r
        if r == 3:
            return l
    if l == 2:
        if r == 1:
            return l
        if r == 3:
            return r
    if l == 3:
        if r == 1:
            return r
        if r == 2:
            return l


# 그룹을 나누는 함수
def tournament(i, j):
    
    # 종료조건
    # 더이상 두 부분으로 쪼갤 수가 없을때 --> i~j까지 사이에 있는 사람이 1명
    if i == j:
        # i번째 사람이라고 return
        return i

    # 재귀호출
    else:
        # 왼쪽부분
        left = tournament(i, (i+j)//2)
        # 오른쪽부분
        right = tournament((i+j)//2+1, j)
        # 왼쪽과 오른쪽에서 승자를 골라서 return
        # cards[left] -> 왼쪽사람이 낸 패
        # cards[right] -> 오른쪽사람이 낸 패

        # 승자를 판별하는 코드
        print(left, right)
        # winner = win(cards[left], cards[right])
        # return winner


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 인원수
    cards = list(map(int, input().split()))

    print(tournament(0,N))
