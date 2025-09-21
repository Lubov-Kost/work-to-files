with open('hw2/gens.txt') as file:
    dom_gom, getero, rec_gom = map(int, file.readline().split())

all_pairs = dom_gom + getero + rec_gom

probability = 1 - (rec_gom*(rec_gom-1) + 0.25*getero*(getero-1) + 
                   getero*rec_gom) / (all_pairs*(all_pairs-1))

with open("hw2/gens.txt", "a") as file:
    file.write('\n' + "Вероятность доминантного аллеля:" + '\n')
    file.write(f'{probability:.5f}')
