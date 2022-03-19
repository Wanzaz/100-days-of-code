
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

height = 0
for n in range(0, n+1):
    height = height + student_heights[n]

average = round(height/(n+1))

print(average)

