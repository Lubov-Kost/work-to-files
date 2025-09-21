with open('hw2/merging.txt') as file:
    length_mas_one = int(file.readline())
    mas_one = list(map(int, file.readline().split()))
    lenght_mas_two = int(file.readline())
    mas_two = list(map(int, file.readline().split()))

sort_mas = []
i = k = 0

while i < length_mas_one or k < lenght_mas_two:
    if i >= length_mas_one:
        sort_mas.append(mas_two[k])
        k += 1
    elif k >= lenght_mas_two:
        sort_mas.append(mas_one[i])
        i += 1
    elif mas_one[i] <= mas_two[k]:
        sort_mas.append(mas_one[i])
        i += 1
    else:
        sort_mas.append(mas_two[k])
        k += 1

sort_mas = ' '.join(map(str, sort_mas))

with open("hw2/most.txt", "a") as file:
    file.write('\n' + "Отсортированный массив:" + '\n')
    file.write(f'{sort_mas}')
