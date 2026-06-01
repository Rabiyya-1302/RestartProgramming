student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for i in student_scores:
    if student_scores[i]>=91:
        student_scores[i]="Outstanding"
    elif student_scores[i]>=81 or student_scores[i]==90:
        student_scores[i]="Exceeds Expectation"
    elif student_scores[i]>=71 or student_scores[i]==80:
        student_scores[i]="Acceptable"
    else:
        student_scores[i]="Fail"
print(student_scores)