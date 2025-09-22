file = open("hw2/graph.txt")
count_vertex, count_costae = map(int, file.readline().split())
ligaments = {}
roommates = {} 

for i in range(1, count_vertex + 1):
    vertex_str = str(i)
    ligaments[vertex_str] = 0
    roommates[vertex_str] = []

for i in range(count_costae):
    costae = file.readline().split()
    first_vertex = costae[0]
    second_vertex = costae[1]
    
    ligaments[first_vertex] += 1
    ligaments[second_vertex] += 1
    
    roommates[first_vertex].append(second_vertex)
    roommates[second_vertex].append(first_vertex)

file.close()

result = []
for i in range(1, count_vertex + 1):
    vertex_str = str(i)
    double_degree = 0
    for roommate in roommates[vertex_str]:
        double_degree += ligaments[roommate]
    result.append(double_degree)

result = ' '.join(map(str, result))

with open("hw2/graph.txt", "a") as file:
    file.write('\n' + "Массив двойной степени:" + '\n')
    file.write(f'{result}') 
