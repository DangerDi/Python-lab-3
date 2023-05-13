point = 15
bagpag = [[0,0,0,0],[0,0,0]]
infection = False
asthma = False
placeIndex = [0,0,0]
weightPoint = []

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


for i in range(5):
    if(i!=4):
        addBagpag(gameObject[weightPoint[i][0]])
    else:
        addBagpag(gameObject[weightPoint[5][0]])
for i in range(6):
    point = point - gameObject[weightPoint[i+6][0]][3]
point = point - gameObject[weightPoint[4][0]][3]

print(bagpag[0])
print(bagpag[1])
print(f'point: {point}')
print('существует как минимум один вариант решения \nзадачи для случая с инвентарем в 7 ячеек')
