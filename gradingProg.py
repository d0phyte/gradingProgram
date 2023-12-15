studentScores = {
    "John": 90,
    "Harry": 81,
    "Jack": 70,
    "Jill": 80,
    "Ron": 102,
    "Jenny": 75,
    "Jerry": 65,
    "Judy": 100,
    "Jeff": 55,
}

studentGrades = {}

for key in studentScores:
    if studentScores[key] <= 70:
        studentGrades[key] = "Fail"
    elif studentScores[key] > 70 and studentScores[key] <= 80 :
        studentGrades[key] = "Acceptable"
    elif studentScores[key] > 80 and studentScores[key] <= 90 :
        studentGrades[key] = "Good"
    elif studentScores[key] > 90 and studentScores[key] <= 100 :
        studentGrades[key] = "Excellent"
    else:
        studentGrades[key] = "This test was graded incorrectly"

print(studentGrades)     