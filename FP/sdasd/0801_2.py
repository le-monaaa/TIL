# T: 노선 수/ N: 종점/ K: 한 번 충전으로 이동가능한 최대 정류장 수/ M: 충전기가 설치된 정류장 번호의 수
# 충전기 설치가 잘못되어 종점에 도착할 수 없다 = 0 출력.

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    stopn = list(map(int, input().split())) #충전기가 있는 정류장 번호

    count = [0] * (N + 1)  #버스정류장
    cnt = charge = 0
    move = K
    temp = []

    for i in stopn:
        count[i] += 1

    for i in range(1, N+1): # 버스정류장 하나에 도착할 때마다
        move -= 1
        if count[i] == 1: # 정류장에 충전기가 있는 경우.
            if N - i < K: # 남은 거리보다 최대 이동거리가 길 때
                print("---------------------")
                print("---------------------")
                for j in range(1, N - i + 1): # 남은 거리만큼만 체크
                    print("j=", j)
                    if count[i+j] == 1:
                        cnt += 1
                        temp.append(i+j)
                        print("temp=",temp)
                if cnt > 0: # 이동거리 내에 충전소가 있으면
                    for n in reversed(temp): #충전소 체크
                        if n - move <= 0: #남은 이동횟수에서 n을 뺐을때 음수면
                            charge += 1
                            move += K

            else: #아닌 경우 그냥 체크
                print("###### ㅁㄹㄴㅁ ######")
                for j in range(1, K + 1): # 최대 이동거리만큼의 정류장 체크
                    # print(f"count[{i+j}]= {count[i + j]}")
                    if count[i+j] == 1:
                        cnt += 1
                        temp.append(i+j)
                if cnt > 0: # 앞으로의 이동거리 내에 충전소가 있는데
                    for n in reversed(temp): # 충전소 정류장 리스트
                        if n - move <= 0: #남은 이동횟수에서 n을 뺐을때 음수다?
                            charge += 1
                            move += K
                        else:
                            break # 기냥 지나가기
                else: # 충전소가 없다!
                    charge += 1
                    move += K
        else: #충전기가 없는 정류장
            continue

    if move < 0: # 이동횟수가 음수가 되면 0 출력
        charge = 0


    print(f"#{t} {charge}")
