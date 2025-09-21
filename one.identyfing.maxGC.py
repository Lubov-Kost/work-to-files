percent = []
names = []
count_gc = 0
count_all = 0
name = ''
file = open('/Users/lu200/OneDrive/Рабочий стол/питон/hw2/fasta.txt')
for line in file:
    line = line.strip()
    if '>' in line:
        if count_all > 0:
            percent_gc = count_gc/count_all * 100
            percent.append(percent_gc)
            names.append(name)
        name = line[1:]
        count_gc = 0
        count_all = 0
    else:
        count_gc += line.count('G') + line.count('C')
        count_all += len(line)

if count_all > 0:
    percent_gc = count_gc/count_all * 100
    percent.append(percent_gc)
    names.append(name)

file.close()

with open('/Users/lu200/OneDrive/Рабочий стол/питон/hw2/fasta.txt', 'a') as file:
    file.write(f'Идентификатор строки с наибольшим содержанием GC: {names[percent.index(max(percent))]}' + '\n')
    file.write(f"Содержание GC этой строки: {max(percent):.6f}")
