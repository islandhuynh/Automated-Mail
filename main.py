with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_template = starting_letter.readlines()

for name in names_list:
    formatted_name = name.strip()
    guest_greeting = letter_template[0].replace("[name]", formatted_name)
    with open(f"Output/ReadyToSend/letter_for_{formatted_name}.txt", mode="w") as letter:
        letter.write(guest_greeting)
        for line_index in range(1, len(letter_template)):
            letter.write(letter_template[line_index])