students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
rank = 1   

scores = []
for student in students:
    if student[1] not in scores:
        scores.append(student[1])

sorted_scores = list(sorted(scores))

rank_score = sorted_scores[rank]
rank_students = []
for student in students:
    if student[1] == rank_score:
        rank_students.append(student)

sorted_rank_students = sorted(rank_students)
for student in sorted_rank_students:
    print(student[0])
