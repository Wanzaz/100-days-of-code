# the highest score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# or you can use the max() function
# max = max(student_scores)
highest = student_scores[0]
for index in range(0, len(student_scores)):
    if student_scores[index] > highest:
        highest = student_scores[index]

print("The highest score in the class is: ", highest)

"""
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print("The highest score in the class is: {highest_score}")
"""
