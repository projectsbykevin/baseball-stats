

def makeList():
    file = open('ejections.csv', 'r')
    list = []
    for line in file:
        data = line.strip().split(',')
        list.append(data)

    return list


def findHighest(list):
    largestTerm = 0
    largestNumber = 0
    for i in range(len(list)):
        if list[i] > largestNumber:
            largestTerm = i
            largestNumber = list[i]
            print(largestTerm)
            print(largestNumber)

    teams = ["Atlanta Braves", "Miami Marlins", "New York Mets", "Philadelphia Phillies", "Washington Nationals", "Chicago Cubs", "Cincinnati Reds", "Milwaukee Brewers", "Pittsburgh Pirates", "St Louis Cardinals", "Arizona Diamondbacks", "Colorado Rockies", "Los Angeles_Dodgers", "San Diego Padres", "San Francisco Giants", "Baltimore Orioles", "Boston Red Sox", "New York Yankees", "Tampa Bay Rays", "Toronto Blue Jays", "Chicago White Sox", "Cleveland Indians", "Detroit Tigers", "Kansas City Royals", "Minnesota Twins", "Houston Astros", "Los Angeles Angels", "Oakland Athletics", "Seattle Mariners", "Texas Rangers"]
    team = teams[largestTerm]
    return team
def counter(list):
    Atlanta_Braves = 0
    Miami_Marlins = 0
    New_York_Mets = 0
    Philadelphia_Phillies = 0
    Washington_Nationals = 0
    Chicago_Cubs = 0
    Cincinnati_Reds = 0
    Milwaukee_Brewers = 0
    Pittsburgh_Pirates = 0
    St_Louis_Cardinals = 0
    Arizona_Diamondbacks = 0
    Colorado_Rockies = 0
    Los_Angeles_Dodgers = 0
    San_Diego_Padres = 0
    San_Francisco_Giants = 0
    Baltimore_Orioles = 0
    Boston_Red_Sox = 0
    New_York_Yankees = 0
    Tampa_Bay_Rays = 0
    Toronto_Blue_Jays = 0
    Chicago_White_Sox = 0
    Cleveland_Indians = 0
    Detroit_Tigers = 0
    Kansas_City_Royals = 0
    Minnesota_Twins = 0
    Houston_Astros = 0
    Los_Angeles_Angels = 0
    Oakland_Athletics = 0
    Seattle_Mariners = 0
    Texas_Rangers = 0

    for i in range(len(list)):
        if list[i][1][:14] == "Atlanta Braves":
            Atlanta_Braves = Atlanta_Braves + 1
        if list[i][1][:13] == "Miami Marlins":
            Miami_Marlins = Miami_Marlins + 1
        if list[i][1][:13] == "New York Mets":
            New_York_Mets = New_York_Mets + 1
        if list[i][1][:21] == "Philadelphia Phillies":
            Philadelphia_Phillies = Philadelphia_Phillies + 1
        if list[i][1][:20] == "Washington Nationals":
            Washington_Nationals = Washington_Nationals + 1
        if list[i][1][:12] == "Chicago Cubs":
            Chicago_Cubs = Chicago_Cubs = 1
        if list[i][1][:15] == "Cincinnati Reds":
            Cincinnati_Reds = Cincinnati_Reds + 1
        if list[i][1][:17] == "Milwaukee Brewers":
            Milwaukee_Brewers = Milwaukee_Brewers + 1
        if list[i][1][:18] == "Pittsburgh Pirates":
            Pittsburgh_Pirates = Pittsburgh_Pirates + 1
        if list[i][1][:18] == "St Louis Cardinals":
            St_Louis_Cardinals = St_Louis_Cardinals + 1
        if list[i][1][:20] == "Arizona Diamondbacks":
            Arizona_Diamondbacks = Arizona_Diamondbacks + 1
        if list[i][1][:16] == "Colorado Rockies":
            Colorado_Rockies = Colorado_Rockies + 1
        if list[i][1][:19] == "Los Angeles Dodgers":
            Los_Angeles_Dodgers = Los_Angeles_Dodgers + 1
        if list[i][1][:16] == "San Diego Padres":
            San_Diego_Padres = San_Diego_Padres + 1
        if list[i][1][:20] == "San Francisco Giants":
            San_Francisco_Giants = San_Francisco_Giants = + 1
        if list[i][1][:17] == "Baltimore Orioles":
            Baltimore_Orioles = Baltimore_Orioles + 1
        if list[i][1][:14] == "Boston Red Sox":
            Boston_Red_Sox = Boston_Red_Sox + 1
        if list[i][1][:16] == "New York Yankees":
            New_York_Yankees = New_York_Yankees + 1
        if list[i][1][:14] == "Tampa Bay Rays":
            Tampa_Bay_Rays = Tampa_Bay_Rays + 1
        if list[i][1][:17] == "Toronto Blue Jays":
            Toronto_Blue_Jays = Toronto_Blue_Jays + 1
        if list[i][1][:17] == "Chicago White Sox":
            Chicago_White_Sox = Chicago_White_Sox + 1
        if list[i][1][:17] == "Cleveland Indians":
            Cleveland_Indians = Cleveland_Indians + 1
        if list[i][1][:14] == "Detroit Tigers":
            Detroit_Tigers = Detroit_Tigers + 1
        if list[i][1][:18] == "Kansas City Royals":
            Kansas_City_Royals = Kansas_City_Royals + 1
        if list[i][1][:15] == "Minnesota Twins":
            Minnesota_Twins = Minnesota_Twins + 1
        if list[i][1][:14] == "Houston Astros":
            Houston_Astros = Houston_Astros + 1
        if list[i][1][:18] == "Los Angeles Angels":
            Los_Angeles_Angels = Los_Angeles_Angels + 1
        if list[i][1][:17] == "Oakland Athletics":
            Oakland_Athletics = Oakland_Athletics + 1
        if list[i][1][:16] == "Seattle Mariners":
            Seattle_Mariners = Seattle_Mariners + 1
        if list[i][1][:13] == "Texas Rangers":
            Texas_Rangers = Texas_Rangers + 1
    teams = [Atlanta_Braves, Miami_Marlins, New_York_Mets, Philadelphia_Phillies, Washington_Nationals, Chicago_Cubs, Cincinnati_Reds, Milwaukee_Brewers, Pittsburgh_Pirates, St_Louis_Cardinals, Arizona_Diamondbacks, Colorado_Rockies, Los_Angeles_Dodgers, San_Diego_Padres, San_Francisco_Giants, Baltimore_Orioles, Boston_Red_Sox, New_York_Yankees, Tampa_Bay_Rays, Toronto_Blue_Jays, Chicago_White_Sox, Cleveland_Indians, Detroit_Tigers, Kansas_City_Royals, Minnesota_Twins, Houston_Astros, Los_Angeles_Angels, Oakland_Athletics, Seattle_Mariners, Texas_Rangers]

    return teams


def main():
    # list = makeList()
    # totals = counter(list)
    # print(totals)
    # top = findHighest(totals)
    # print(top)
    # print("the "+str(top)+" have the highest number of ejections since 2015")
    w1 = input("word 1:")
    print(w1)
main()
