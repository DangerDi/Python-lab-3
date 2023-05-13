import itertools
point = 15
bagpag = [[0,0,0,0],[0,0,0,0]]
infection = False
asthma = False
placeIndex = [0,0,0]
weightPoint = []
var1 = [[[0,1,2,3,4,6],[5,7,8,9,10,11]],[[0,1,2,3,7],[4,5,6,8,9,10,11]],
        [[0,1,2,3,4,8],[5,7,6,9,10,11]],[[0,1,2,3,4,9], [5,7,6,8,10,11]],
        [[0,1,2,3,10], [5,7,6,9,4,8,11]],[[0,1,2,4,9,8], [5,7,6,3,10,11]],
        [[0,1,2,4,9,8], [5,7,6,3,10,11]],[[0,1,2,3,10], [5,7,6,4,8,9,11]],]
gameObject = [['Винтовка','в', 3, 25 ], ['Пистолет','п', 2, 15 ],
              ['Боекомплект','б', 2, 15 ], ['Аптечка','а', 2, 20 ],
              ['Ингалятор','и', 1, 0 ], ['Нож','н', 1, 15 ],
              ['Топор','т', 3, 20 ], ['Оберег','о', 1, 25 ],
              ['Фляжка','ф', 1, 15 ], ['Антидот','д', 1, 10 ],
              ['Еда','к', 2, 20 ], ['Арбалет','р', 2, 20 ]]
# функция добавления предмета в рюкзак
def addBagpag(gameObject):
    global placeIndex
    global point
    place = gameObject[2]
    marker = True
    for i in range(place):
        if (placeIndex[0] >= 4):
            placeIndex[2] = 1
            break
        if (place <= 4 - placeIndex[0] and marker):
            point += gameObject[3]
            marker = False
        bagpag[0][placeIndex[0]]=gameObject[1]
        placeIndex[0] += 1
        place -= 1

    if(placeIndex[2] == 1):
        if(place > 0):
            if(place <= 4-placeIndex[1]):
                point += gameObject[3]
                for i in range(place):
                    if (placeIndex[1] >= 4):
                        break
                    bagpag[1][placeIndex[1]]=gameObject[1]
                    placeIndex[1] += 1

# функция для сортировки
def custom_key(weight):
    return weight[2]

if(infection):
    addBagpag(gameObject[9])
if(asthma):
    addBagpag(gameObject[4])

#сортировка предметов по ценности игровых очков
for i in range(12):
    weightPoint.append([i, gameObject[i][2], gameObject[i][3]/gameObject[i][2]])
weightPoint.sort(key=custom_key, reverse=True)

for i in range(6):
    addBagpag(gameObject[weightPoint[i][0]])
for i in range(6):
    point = point - gameObject[weightPoint[i+6][0]][3]

print(bagpag[0])
print(bagpag[1])
print(f'point: {point}')
print('\nДополниетельное задание, все возможные \nварианты положительного итора игры')

for i in range(len(var1)):
    bagpag = [[0,0,0,0],[0,0,0,0]]
    point = 15
    placeIndex = [0,0,0]
    for j in range(len(var1[i][0])):
        addBagpag(gameObject[weightPoint[var1[i][0][j]][0]])
    for j in range(len(var1[i][1])):
        point = point - gameObject[weightPoint[var1[i][1][j]][0]][3]

    if(point > 0):
        print(bagpag[0])
        print(bagpag[1])
        print(f'point: {point}\n')
