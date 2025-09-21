file = open('hw2/most.txt')
a, b = map(int, file.readline().split())
occurring_more = []
for i in range(a):
    repeats = {}
    one_line = file.readline().split()
    flag = False
    for k in one_line:
        if k in repeats:
            repeats[k] += 1
            if repeats[k] > b/2:
                occurring_more.append(int(k))
                flag = True
                break
        else:
            repeats[k] = 1
    if flag == False:
        occurring_more.append(-1)

file.close()

occurring_more = ' '.join(map(str, occurring_more))

with open("hw2/most.txt", "a") as file:
    file.write('\n' + "Элементы массивов, встречающиеся чаще вего:" + '\n')
    file.write(f'{occurring_more}')
