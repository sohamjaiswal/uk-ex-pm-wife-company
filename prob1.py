totalMonsters = int(input("Enter the total number of monsters: "))
initialExp = int(input("Enter the initial experience: "))
powerLevels = [] # his power level is over 9000!!!
exps = []
for i in range(0, totalMonsters):
    monsterPower = int(input("Enter the power of monster " + str(i + 1) + ": "))
    powerLevels.append(monsterPower)
for i in range(0, totalMonsters):
    earnableExp = int(input("Enter the experience earned by defeating monster " + str(i + 1) + ": "))
    exps.append(earnableExp)
monsterPowerExps = []
for i in range(0, totalMonsters):
    monsterPowerExps.append((powerLevels[i], exps[i]))
monsterPowerExps.sort(key=lambda x: x[0])
defeated = 0
for i in range(0, totalMonsters):
    if monsterPowerExps[i][0] <= initialExp:
        defeated += 1
        initialExp += monsterPowerExps[i][1]
print(defeated)