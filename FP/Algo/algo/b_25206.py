# baejoon 25206 너의 평점은 https://www.acmicpc.net/problem/25206
# 전공평점; 전공과목별 (SUM(학점*과목평점))/학점 총합
# 과목명/학점/등급 (공백구분, P는 제외)
# 과목명-알파벳 대소문자 or 숫자, 공백x 중복값x
# 학점- 1.0, 2.0, 3.0, 4.0
# 등급- A+, A0, B+, B0, C+, C0, D+, D0, F, P
grade_score, total_score = 0, 0
grade_point = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0
}
for i in range(20):
    score = list(input().split())
    # print(score)
    if score[2] != "P":
        total_score += float(score[1])
        grade_score += (float(score[1])*grade_point[score[2]])

print(round((grade_score/total_score), 6))
