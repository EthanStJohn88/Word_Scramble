def main():
	userNum = welcomeUser()
	print()

	if userNum == 1:
		calculator()
		
	elif userNum == 2:
		groceryList()



def welcomeUser():
	print("Welcome! I am PASS-bot. What would you like to do today?")
	print()

	menu = ["1: Calculator", "2: Grocery list"]

	for i in range(len(menu)):
		print(menu[i])

	print()
	answer = int(input("Please select a number: "))
	
	return answer


def calculator():
	x = int(input("Please enter a number: "))
	print()
	y = int(input("Please enter a number: "))
	
	operations = ["1: add", "2: subtract", "3: multiply", "4: divide", "5: exponentiation"]
	
	for operation in operations:
		print(operation)
	
	print()
	
	op = int(input("Which operation would you like to perform? "))
	
	if op == 1:
		z = x + y
		
	elif op == 2:
		z = x - y
		
	elif op == 3:
		z = x * y
		
	elif op == 4:
		z = x / y
		
	elif op == 5:
		z = x ** y
		
	
	print(z)
	
	
def groceryList():
#Load grocery list
	#read in grocery file (weeklyGroceries.txt) and parse into parallel lists
	
	groceryList = []
	numGroceries = []
	
	inputFile = open("weeklyGroceries.txt", 'r')
	allTheLines = inputFile.readlines()
	
	for i in range(len(allTheLines)):		
		eachLine = allTheLines[i].split(',')
		
		if eachLine[1].strip() == "0":
			True
			
		else:
			groceryList.append(eachLine[0])
			numGroceries.append(eachLine[1].strip())
	
	
	for i in range(len(groceryList)):
		print(groceryList[i] + ' ' + str(numGroceries[i]))
	

#Allow user to make modifications
	userMod = input("Would you like to make changes? Enter Y or N: ")
	
	while userMod == 'Y' or userMod == 'y':
		print()
		userGroceryItem = input("Enter grocery item: ")
		userItemQty = int(input("how many? "))
		print()
		
		#If item exists, change num. Else, add item & number
		itemExists = False
		for i in range(len(groceryList)):
			if groceryList[i] == userGroceryItem:
				numGroceries[i] = userItemQty
				itemExists = True
				
				if userItemQty == 0:
					del groceryList[i]
					del numGroceries[i]
					break
		
		if itemExists == False:
			if userItemQty == 0:
				0 == 0
				
			else:
				groceryList.append(userGroceryItem)
				numGroceries.append(userItemQty)

		
		for i in range(len(groceryList)):
			print(groceryList[i] + ' ' + str(numGroceries[i]))
			
		userMod = input("\nWould you like to make any more changes? Enter Y or N: ")
		
	#Write updated list to output file (weeklyGroceries.txt)
		outFile = open("weeklyGroceries.txt", 'w')
		
		for i in range(len(groceryList)):
			outFile.write(groceryList[i] + ',' + str(numGroceries[i]) + "\n")
	
	return

	
	
	
	
	
	
	
	
main()