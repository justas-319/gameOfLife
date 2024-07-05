from time import sleep

# rows = int(input("Aukstis: "))
# columns = int(input("Ilgis: "))

# playfield = []

# for i in range(rows):
#     a = []
#     for j in range(columns):
#         a.append(0)
#     playfield.append(tuple(a))

# playfield = tuple(playfield)

# pardinis zaidimo issidestymas, 0 - mirusios dalys, 1 - gyvos. Zaidima galima isplesti padidinant tuplus
playfield = (
    (0, 1, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0)
)

# kaip greitai eina zaidimas
delayTime = 1

# kiek generaciju i prieki
generations = 5

newPlayfield = []

# pitonas sukeite x su y, y eina pirmas koordinates uzrasomos y, x
rows = len(playfield)
columns = len(playfield[0])

def topLeftCorner(alive):
    isAlive = 0
    if playfield[0][1] == 1:
        isAlive += 1
    if playfield[1][0] == 1:
        isAlive += 1
    if playfield[1][1] == 1:
        isAlive += 1
    # tikrinam ar buvo gyva
    if alive == 1:
        if isAlive >= 2:
            return(1)
        else:
            return(0)
    else:
        if isAlive == 3:
            return(1)
        else:
            return(0)

def topRightCorner(alive):
    isAlive = 0
    # columns -2 nes columns -1 yra dabartinis o man reikia praito
    if playfield[0][columns - 2] == 1:
        isAlive += 1
    if playfield[1][columns - 1] == 1:
        isAlive += 1
    if playfield[1][columns - 2] == 1:
        isAlive += 1
    # tikrinam ar buvo gyva
    if alive == 1:
        if isAlive >= 2:
            return(1)
        else:
            return(0)
    else:
        if isAlive == 3:
            return(1)
        else:
            return(0)

def bottomLeftCorner(alive):
    isAlive = 0
    # columns -2 nes columns -1 yra dabartinis o man reikia praito
    if playfield[rows - 2][0] == 1:
        isAlive += 1
    if playfield[rows - 2][1] == 1:
        isAlive += 1
    if playfield[rows - 1][1] == 1:
        isAlive += 1
    # pasirenkam ar buvo gyva
    if alive == 1:    
        if isAlive >= 2:
            return(1)
        else:
            return(0)
    else:
        if isAlive == 3:
            return(1)
        else:
            return(0)

def bottomRightCorner(alive):
    isAlive = 0
    if playfield[rows - 1][columns - 2] == 1:
        isAlive += 1
    if playfield[rows - 2][columns - 1] == 1:
        isAlive += 1
    if playfield[rows - 2][columns - 2] == 1:
        isAlive += 1
    if alive == 1:
        if isAlive >= 2:
            return(1)
        else:
            return(0)
    else:
        if isAlive == 3:
            return(1)
        else:
            return(0)

def topSide(alive, x, y):
    isAlive = 0
    if playfield[y][x - 1] == 1:
        isAlive += 1
    if playfield[y][x + 1] == 1:
        isAlive += 1
    if playfield[y + 1][x - 1] == 1:
        isAlive += 1
    if playfield[y + 1][x] == 1:
        isAlive += 1
    if playfield[y + 1][x + 1] == 1:
        isAlive += 1
    # tikrinam ar alive
    if alive == 1:
        if isAlive == 2 or isAlive == 3:
            return(1)
        else:
            return(0)
    else:
        if isAlive == 3:
            return(1)
        else:
            return(0)

def bottomSide(alive, x, y):
    isAlive = 0
    if playfield[y][x - 1] == 1:
        isAlive += 1
    if playfield[y][x + 1] == 1:
        isAlive += 1
    if playfield[y - 1][x - 1] == 1:
        isAlive += 1
    if playfield[y - 1][x] == 1:
        isAlive += 1
    if playfield[y - 1][x + 1] == 1:
        isAlive += 1
    # tikrinam ar alive
    if alive == 1:
        if isAlive == 2 or isAlive == 3:
            return(1)
        else:
            return(0)
    else:
        if isAlive == 3:
            return(1)
        else:
            return(0)

def leftSide(alive, x, y):
    isAlive = 0
    if playfield[y - 1][x] == 1:
        isAlive += 1
    if playfield[y - 1][x + 1] == 1:
        isAlive += 1
    if playfield[y][x + 1] == 1:
        isAlive += 1
    if playfield[y + 1][x + 1] == 1:
        isAlive += 1
    if playfield[y + 1][x] == 1:
        isAlive += 1
    # tikrinam ar alive
    if alive == 1:
        if isAlive == 2 or isAlive == 3:
            return(1)
        else:
            return(0)
    else:
        if isAlive == 3:
            return(1)
        else:
            return(0)

def rightSide(alive, x, y):
    isAlive = 0
    if playfield[y - 1][x] == 1:
        isAlive += 1
    if playfield[y - 1][x - 1] == 1:
        isAlive += 1
    if playfield[y][x - 1] == 1:
        isAlive += 1
    if playfield[y + 1][x - 1] == 1:
        isAlive += 1
    if playfield[y + 1][x] == 1:
        isAlive += 1
    # tikrinam ar alive
    if alive == 1:
        if isAlive == 2 or isAlive == 3:
            return(1)
        else:
            return(0)
    else:
        if isAlive == 3:
            return(1)
        else:
            return(0)

# problema kazkur cia panasu kazkur keiciamas playfield o neturetu buti jis keiciamas
def centre(alive, x, y):
    isAlive = 0
    # N
    if playfield[y - 1][x] == 1:
        isAlive += 1
    # NE
    if playfield[y - 1][x + 1] == 1:
        isAlive += 1
    # E
    if playfield[y][x + 1] == 1:
        isAlive += 1
    # SE
    if playfield[y + 1][x + 1] == 1:
        isAlive += 1
    # S
    if playfield[y + 1][x] == 1:
        isAlive += 1
    # SW
    if playfield[y + 1][x - 1] == 1:
        isAlive += 1
    # W
    if playfield[y][x - 1] == 1:
        isAlive += 1
    # NW
    if playfield[y - 1][x - 1] == 1:
        isAlive += 1
    # tikrinam ar alive
    if alive == 1:
        if isAlive == 2 or isAlive == 3:
            return(1)
        else:
            return(0)
    else:
        if isAlive == 3:
            return(1)
        else:
            return(0)


# print initial setup
for i in range(rows):
    newPlayfield.append([])
    for j in range(columns):
        newPlayfield[i].append(0)
for i in range(rows):
    print(playfield[i])
print()

# main game loop
sleep(1)
for i in range(generations):
    for y in range(rows):
        for x in range(columns):
            # kampai
            if y == 0 and x == 0:
                newPlayfield[y][x] = topLeftCorner(playfield[y][x])
            elif y == 0 and x == columns - 1:
                newPlayfield[y][x] = topRightCorner(playfield[y][x])
            elif y == rows - 1 and x == 0:
                newPlayfield[y][x] = bottomLeftCorner(playfield[y][x])
            elif y == rows -1 and x == columns - 1:
                newPlayfield[y][x] = bottomRightCorner(playfield[y][x])
            # krastai
            elif y == 0 and x+1 < columns:
                newPlayfield[y][x] = topSide(playfield[y][x], x, y)
            elif y == rows - 1:
                newPlayfield[y][x] = bottomSide(playfield[y][x], x, y)
            elif x == 0:
                newPlayfield[y][x] = leftSide(playfield[y][x], x, y)
            elif x == columns - 1:
                newPlayfield[y][x] = rightSide(playfield[y][x], x, y)
            else:
                newPlayfield[y][x] = centre(playfield[y][x], x, y)

    playfield = list(playfield)

    for j in range(rows):
        playfield[j] = tuple(newPlayfield[j])
        print(newPlayfield[j])
    print()
    sleep(delayTime)
    playfield = tuple(playfield)