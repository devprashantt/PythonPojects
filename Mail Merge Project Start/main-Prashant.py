PLACEHOLDER = "[name]"

with open ("./Input/names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt ", mode='w') as completed_letters:
            completed_letters.write(new_letter)
