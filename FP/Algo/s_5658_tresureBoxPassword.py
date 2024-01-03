import sys;sys.stdin = open("../5658.txt", "r")

# SWEA 5658 보물상자 비밀번호
# 16진수 숫자가 적힌 보물상자. 시계방향으로 돌아가고 한 번 돌리면 한 칸씩 회전 -> 왜 이딴 걸?
# 시계방향 순으로 높은 자리 숫자에 해당하며 하나의 수를 나타냄.
# 비밀번호: 보물상자에 적힌 숫자로 만들 수 있는 모든 수 중 K번째로 큰수를 10진수로 만든 수
# N개의 숫자 입력-> 비밀번호 출력///////////////////아니왜???????????????????????????
# N은 4의 배수. 8<= N <= 28, 중복 수 주의
# T/N, K/ N hex nums

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    lst = list(input())

    # 16진수 상태의 수를 저장
    hex_num = set()
    # 회전횟수 n//3 한 번 끝날 때마다 회전하면서
    for s in range(n//4):
        for i in range(0, len(lst), n//4):
            hex_num.add("".join(lst[i:i+n//4]))
        lst.insert(0, lst.pop())

    # 정렬할 리스트
    dec_num = []
    # 마지막에 리스트로 바꿔서 10진수화, 정렬해서 k번째 출력
    for hex in hex_num:
        dec_num.append(int(hex, 16))

    dec_num.sort(reverse=True)

    print(f"#{tc} {dec_num[k-1]}")
