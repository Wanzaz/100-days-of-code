# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# Assigning random score to each student
students_score = {student:random.randint(1, 100) for student in names}

# Putting passed students in another dict
passed_students = {student:score for (student, score) in students_score.items() if score >= 60}
print(passed_students)


