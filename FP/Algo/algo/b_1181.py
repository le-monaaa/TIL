# baekjoon 1181 단어 정렬 https://www.acmicpc.net/problem/1181
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오
# 짧은 것부터, 길이가 같으면 사전 순으로/ 중복제거

words = set()
max_len = 0
N = int(input())
for n in range(N):
    word = input()
    words.add(word)
    if len(word) > max_len:
        max_len = len(word)
word_list = [[] for _ in range(max_len)]
for word in words:
    word_list[len(word)-1].append(word)

for l in word_list:
    l = sorted(l)
    for i in range(len(l)):
        print(l[i])