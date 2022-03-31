student_scores = { 
	"Harry": 81,
	"Ron": 78,
	"Hermione": 99, 
	"Draco": 74,
	"Neville": 62,
}

student_grades = {}

for key in student_scores:
	student = student_scores[key]
	if student > 90:
		student_grades[key] = 'Outstanding'
	elif student > 80:
		student_grades[key] = 'Exceeds Expectations'
	elif student > 70:
		student_grades[key] = 'Acceptable'
	elif student_scores[key] < 70:
		student_grades[key] = 'Fail'

print(student_grades)
