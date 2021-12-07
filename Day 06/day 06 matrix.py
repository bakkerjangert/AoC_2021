import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

# Even afgezien van de condensatie om het aantal regels te minimaliseren,
# komt het neer op de matrix-notatie van de recursieve functies. Bij elke tijdstap geldt:
# vis(bevalt over 0 dagen,tijdstip t+1)=vis(bevalt over 1 dag ,tijdstip t)
# vis(bevalt over 1 dag ,tijdstip t+1)=vis(bevalt over 2 dagen,tijdstip t)
# vis(bevalt over 2 dagen,tijdstip t+1)=vis(bevalt over 3 dagen,tijdstip t)
# vis(bevalt over 3 dagen,tijdstip t+1)=vis(bevalt over 4 dagen,tijdstip t)
# vis(bevalt over 4 dagen,tijdstip t+1)=vis(bevalt over 5 dagen,tijdstip t)
# vis(bevalt over 5 dagen,tijdstip t+1)=vis(bevalt over 6 dagen,tijdstip t)
# vis(bevalt over 6 dagen,tijdstip t+1)=vis(bevalt over 7 dagen,tijdstip t)+vis(bevalt over 0 dagen,tijdstip t)
# vis(bevalt over 7 dagen,tijdstip t+1)=vis(bevalt over 8 dage,tijdstip tn)
# vis(bevalt over 8 dagen,tijdstip t+1)=vis(bevalt over 0 dagen,tijdstip t)

matrix = np.zeros((9, 9), object)
for i in range(8):
    matrix[i][i + 1] = 1
matrix[6][0] = 1
matrix[8][0] = 1
print(matrix)

matrix = matrix.transpose()
data = []

for i in range(9):
    data.append(lines[0].split(',').count(str(i)))

data_np = np.array(data, object)

days = [80, 256, 1024]

for day in range(max(days)):
    data_np = np.dot(data_np, matrix)
    if day + 1 in days:
        print(f' There are {data_np.sum()} fishes on day {day + 1}')
