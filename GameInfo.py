

def createList():
    file = open('GameInfo.txt', 'r')
    list = []
    for line in file:
        data = line.strip().split(',')
        list.append(data)

    dict = {}
    for i in range(len(list)):
        dict[i] = list[i]
    return dict

def averageLength(dictionary):
    totalTime = 0
    for i in range(len(dictionary)):
        totalTime = totalTime + int(dictionary[i][4])
    avg = totalTime / 9718
    return avg

def averageRunTeam(dictionary):
    Teams = {}
    for i in range(len(dictionary)):
        currentTeam = dictionary[i][13]
        currentRuns = Teams.get(currentTeam)
        if (currentRuns == None):
            currentRuns = 0
        currentRunsInt = int(currentRuns)
        Teams[currentTeam] = currentRuns + int(dictionary[i][6])

    return Teams

def totalGamesTeam(dictionary):
    Teams = {}
    for i in range(len(dictionary)):
        currentTeam = dictionary[i][13]
        currentgames = Teams.get(currentTeam)
        if (currentgames == None):
            currentgames = 0
        currentgamesInt = int(currentgames)
        Teams[currentgames] = currentgames + 1

    return Teams
def averageAway(dictionary):
    totalRuns = 0
    for i in range(len(dictionary)):
        totalRuns = totalRuns + int(dictionary[i][1])
    avg = totalRuns / 9718
    print(avg)

def averageHome(dictionary):
    totalRuns = 0
    for i in range(len(dictionary)):
        totalRuns = totalRuns + int(dictionary[i][6])
    avg = totalRuns / 9718
    print(avg)

def averageAttendence(dictionary):
    total = 0
    for i in range(len(dictionary)):
        total = total + int(dictionary[i][0])
    avg = total / 9718
    print(avg)

def main():
    dictionary = createList()
    totalRunTeamDict = averageRunTeam(dictionary)
    totalGamesTeamDict = totalGamesTeam(dictionary)
    averageTime = averageLength(dictionary)
    print(totalRunTeamDict)
    print(totalGamesTeamDict)
    averageAway(dictionary)
    averageHome(dictionary)
    averageAttendence(dictionary)
main()
