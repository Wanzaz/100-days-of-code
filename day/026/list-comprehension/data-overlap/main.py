# First file numbers
with open('file1.txt') as file1:
    file1_data = file1.readlines()

# Second file numbers
with open('file2.txt') as file2:
    file2_data = file2.readlines()

# Comparing them
# result = [num1 for num1, num2 in zip(file1_data, file2_data) if num1==num2]
result = [int(num) for num in file1_data if num in file2_data]

# result = []
# for num1 in file1_data:
#     if num1 in file2_data:
#         result.append(int(num1)



# Write your code above 👆

print(result)



