# SEWA 16639 피자굽기
# N개의 피자를 동시조리. 완성되는 시간이 다른데 먼저 완성되는 것부터 꺼냄. 제일 마지막 피자 번호
# 1번위치에서 출입,m개의 숫자가 주어지고, 이들은 한바퀴 후 절반이 됨.
# 모두 녹아 0이되면 화덕에서 꺼냄. 남은 피자를 순서대로 넣음.
# T/ N(화덕의 크기),M(피자개수)/Ci
import sys
sys.stdin = open("si2.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # N은 오븐 크기, M 은 피자 개수
    N, M = map(int, input().split())

    # 우리가 구워야할 피자들의 치즈 정보
    pizza_list = list(map(int, input().split()))

    # 다음에 꺼내올 피자 인덱스
    next_i = 0

    # 오븐을 큐로 만들어보자
    oven = [0] * 1000
    ofront = orear = -1

    # 오븐의 크기만큼 피자 넣어주기
    for i in range(N):
        # 오븐에 피자 넣기
        orear += 1
        # 나중에 꺼낼때를 위해서 피자 번호도 같이 넣기
        oven[orear] = [i, pizza_list[i]]  # [피자 번호, 치즈 양]
        next_i += 1

    # 오븐에 남아있는 피자의 개수
    remain = N
    # 마지막에 꺼낸 피자의 번호
    last_idx = -1

    # 모든 피자의 치즈가 녹을때까지 반복
    while True:
        # 피자를 하나 꺼내서
        ofront += 1
        pizza_idx, pizza = oven[ofront]

        # 치즈를 녹이고 c // 2
        pizza //= 2
        # pizza = pizza // 2

        # 남은 치즈 양이 0이 아니다 ==> 다시 오븐에 넣기
        if pizza != 0:
            orear += 1
            oven[orear] = [pizza_idx, pizza]  # [피자 번호, 피자 치즈]

        # 남은 치즈 양이 0이 되었다
        else:
            # 현재 오븐의 자리에 남은피자 하나 꺼내서 넣기
            if next_i < M:
                orear += 1
                oven[orear] = [next_i, pizza_list[next_i]]
                # 하나 꺼냈으니까 다음에 꺼내올 피자 번호 1 증가
                next_i += 1

            # 넣을 피자가 없다
            else:
                remain -= 1
                # 오븐에 남은 피자도 없는 상황이 온다
                if remain == 0:
                    # 현재 피자의 번호가 답이 된다.
                    last_idx = pizza_idx
                    # 답을 구하고
                    # 반복 종료
                    break

    print(f"#{tc} {last_idx + 1}")