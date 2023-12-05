def transform(cubesLine: str) -> (int, list):
    result = []
    cubes = cubesLine.split(':')
    gameId = int(cubes[0].strip()[5:])
    cubes = cubes[1].split(';')
    cubes = [cube.split(',') for cube in cubes] #[['5 red', ' 2 blue', ' 6 green'], [...], ...]    
    for cubeSet in cubes:
        cubesDict = {}
        oneSet = {}
        for cubeTuple in cubeSet:
            cubes = cubeTuple.split()
            cubesDict = {cubes[1].strip()[0]:int(cubes[0].strip())}
            oneSet.update(cubesDict)
        result.append(oneSet)
    return gameId, result

def findMaxCubes(cubes: list) -> dict:
    maxCubes = {}
    cubeDict = {}
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    for cubeDict in cubes:
        if 'r' in cubeDict.keys():
            maxRed = max(maxRed, cubeDict['r'])
        if 'g' in cubeDict.keys():
            maxGreen = max(maxGreen, cubeDict['g'])
        if 'b' in cubeDict.keys():
            maxBlue = max(maxBlue, cubeDict['b'])
    maxCubes = {'r':maxRed, 'g':maxGreen, 'b':maxBlue}
    return maxCubes

#Ensure: 12 red cubes, 13 green cubes, and 14 blue cubes
check = {'r':12, 'g':13, 'b':14}

def compare(maxCubes: dict) -> bool:
    for key in maxCubes.keys():
        if maxCubes[key] > check[key]:
            return False
    return True

def getPower(cubes: dict) -> int:
    power = 1
    for key in cubes.keys():
        power *= cubes[key]
    return power

count = 0
gameId = None
power = 0
with open("day2/day2.txt") as f:
    for line in f.readlines():
        line = line.rstrip('\n')
        gameId, transformed = transform(line)
        maxCubes = findMaxCubes(transformed)
        if compare(maxCubes):
            count += gameId
        power += getPower(maxCubes)
print(count)
print(power)

