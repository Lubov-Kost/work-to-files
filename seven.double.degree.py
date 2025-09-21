file = open("hw2/graph.txt")
count_degree, count_costae = map(int, file.readline().split())
ligaments = {}
roommates = {} 

for i in range(1, count_degree + 1):
    vertex_str = str(i)
    ligaments[vertex_str] = 0
    roommates[vertex_str] = []

for i in range(count_costae):
    costae = file.readline().split()
    first_degrees = costae[0]
    second_degrees = costae[1]
    
    ligaments[first_degrees] += 1
    ligaments[second_degrees] += 1
    
    roommates[first_degrees].append(second_degrees)
    roommates[second_degrees].append(first_degrees)

file.close()

result = []
for vertex in range(1, count_degree + 1):
    vertex_str = str(vertex)
    total = 0
    for neighbor in roommates[vertex_str]:
        total += ligaments[neighbor]
    result.append(total)

result = ' '.join(map(str, result))

with open("hw2/graph.txt", "a") as file:
    file.write('\n' + "Массив двойной степени:" + '\n')
    file.write(f'{result}') 
