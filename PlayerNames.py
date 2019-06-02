import csv
import matplotlib.pyplot as plt 

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


def getPopularFirstNamesDict(firstNames):
	firstNameDict = {}
	popularNames = []
	for name in firstNames:
		if name in firstNameDict:
			firstNameDict[name] = firstNameDict.get(name)+1
		else:
			firstNameDict[name] = 1
	return firstNameDict

def plotPopularFirstNames(firstNames, threshold):
	firstNameDict = getPopularFirstNamesDict(firstNames)
	# x-coordinates of left sides of bars  
	left = [1, 2, 3, 4, 5] 
	  
	# heights of bars 
	height = [10, 24, 36, 40, 5] 
	  
	# labels for bars 
	tick_label = ['one', 'two', 'three', 'four', 'five'] 
	  
	# plotting a bar chart 
	plt.bar(left, height)
	  
	# naming the x-axis 
	plt.xlabel('x - axis') 
	# naming the y-axis 
	plt.ylabel('y - axis') 
	# plot title 
	plt.title('My bar chart!')
	plt.xticks(left,tick_label) 
	  
	# function to show the plot 
	plt.show()  



def main():
	firstNames = firstName()
	#mostCommonName(firstNames)
	plotPopularFirstNames(firstNames,5)


main()