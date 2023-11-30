# baekjoon 2869 달팽이는 올라가고 싶다 https://www.acmicpc.net/problem/2869
# V미터 나무 막대, 낮에 A미터 오르고 밤에 B미터 미끄러짐. 정상 올라가면 안미끄러짐-->???
# A, B, V

A, B, V = map(int, input().split()) # A:하루에 오르는 거리 B:미끄러지는 거리 V: 목표 높이
day = 1
result = (V-B)/(A-B)
if result != int(result):
    print(int(result)+1)
else:
    print(int(result))
