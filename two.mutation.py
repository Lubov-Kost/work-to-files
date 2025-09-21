sequences = ''
with open("hw2/mutation.txt") as file:
    for line in file:
        sequences += line.strip()

lenght_one_sequence = len(sequences) // 2
number_of_discrepancies = 0
for i in range(lenght_one_sequence):
    element_first_line = sequences[i]
    element_second_line = sequences[i+lenght_one_sequence]
    if element_first_line != element_second_line:
        number_of_discrepancies += 1

with open("hw2/mutation.txt", "a") as file:
    file.write('\n' + "Расстояние Хэмминга:" + '\n')
    file.write(f'{number_of_discrepancies}')
