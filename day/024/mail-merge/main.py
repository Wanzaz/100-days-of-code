PLACE_HOLDER = "[name]"

def change_name(name_of_person):
    """Opens letter pattern and replaces the [name] to name_of_person"""
    with open("./input/letters/starting_letter.txt") as letter_pattern:
        content = letter_pattern.read()
    content = content.replace(PLACE_HOLDER, f"{name_of_person}")

    # Save the letters in the folder "ReadyToSend".
    # create a new letter with new name
    with open(f'./output/ready-to-send/letter_for_{name_of_person}.txt', 'w') as new_letter:
      new_letter.write(content)

# For each name in invited_names.txt
with open("./input/names/invited_names.txt") as names_file:
    names = [name.rstrip() for name in names_file]

for name in names:
    # Replace the [name] placeholder with the actual name
    change_name(name)







"""
# Version 1.1 (better)


PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
"""

