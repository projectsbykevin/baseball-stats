import csv

def firstName():
	with open('player_names.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		firstNames = []
		for row in readCSV:
			#print(row)
			firstName = row[1]
			firstNames.append(firstName)
		#print(firstNames)
		return firstNames

def mostCommonName(firstNames):
	mostCommonName = ""
	maxCount = 0
	firstNameDict = {}
	for name in firstNames:
		if name in firstNameDict:
			firstNameDict[name] = firstNameDict.get(name)+1
			if firstNameDict.get(name) > maxCount:
				maxCount = firstNameDict.get(name)
				mostCommonName = name
		else:
			firstNameDict[name] = 1
	print("The most common name is:")
	print(mostCommonName)
	print("with a frequency of:")
	print(maxCount)

def main():
	firstNames = firstName()
	mostCommonName(firstNames)


main()