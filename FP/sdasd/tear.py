# T: 노선 수/ N: 종점/ K: 한 번 충전으로 이동가능한 최대 정류장 수/ M: 충전기가 설치된 정류장 번호의 수
# 충전기 설치가 잘못되어 종점에 도착할 수 없다 = 0 출력.

T = int(input())

def drive(K, N):
    # return ==



for t in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split())) #충전기가 있는 정류장 번호

