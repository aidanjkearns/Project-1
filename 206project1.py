import os
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	listofdict = list()
	import csv
	with open(file) as csvfile:
		dictionary = csv.DictReader(csvfile)
		for entry in dictionary:
			listofdict.append(entry)
	return(listofdict)


	

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	if col is 'First':
		sortfirst = sorted(data, key = lambda x: x['First'])
		firstname = str(sortfirst[0]['First'])
		lastname = str(sortfirst[0]['Last'])
		name = firstname + ' ' + lastname
		return name
	if col is 'Last':
		sortlast = sorted(data, key = lambda x: x['Last'])
		firstname = str(sortlast[0]['First'])
		lastname = str(sortlast[0]['Last'])
		name = firstname + ' ' + lastname
		return name
	if col is 'Email':
		sortemail = sorted(data, key = lambda x: x['Email'])
		firstname = str(sortemail[0]['First'])
		lastname = str(sortemail[0]['Last'])
		name = firstname + ' ' + lastname
		return name

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	grades = list()
	for entry in data:
		grades.append(entry['Class'])
	count = {'Senior':0, 'Junior': 0, 'Sophomore':0, 'Freshman':0}
	for entry in grades:
		count[entry] = count[entry] + 1
	tup = list()
	for hsclass, value in count.items():
		tup.append((hsclass, value))
	tup = sorted(tup, key = lambda x: x[1], reverse = True)
	return tup






# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	dates = list()
	for entry in a:
		dates.append(entry['DOB'])
	days = list()
	import re
	for entry in dates:
		entry = entry.rstrip()
		days = days + re.findall('\/(\S+)\/', entry)
	freq = list()
	for day in days:
		freq.append(int(day))
	common_dict = dict()
	for fre in freq:
		if fre not in common_dict:
			common_dict[fre] = 1
		else:
			common_dict[fre] = common_dict[fre] + 1
	tupl = list()
	for key, val in common_dict.items():
		tupl.append((val, key))
	tupl.sort(reverse=True)
	return(tupl[0][1])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	l = list()
	for entry in a:
		l.append(entry['DOB'])
	newl = list()
	for day in l:
		newl.append(day.split("/"))
	bdays = [list(map(int,x)) for x in newl]
	from datetime import date
	cur_age = list()
	for bday in bdays:
		age = date.today() - date(bday[2],bday[0],bday[1])
		cur_age.append(age.days/365.25)
	return(round(sum(cur_age)/len(cur_age)))
#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	import csv
	shortened = list()
	for person in a:
		shortened.append({'First': person['First'],'Last': person['Last'],'Email': person['Email'] + "\n"})
	keys = shortened[0].keys()
	if col is 'First':
		sortfirst = sorted(shortened, key = lambda x: x['First'])
		with open(fileName, 'w') as output:
			csv_file = csv.DictWriter(output,keys)
			csv_file.writerows(sortfirst)
	if col is 'Last':
		sortlast = sorted(shortened, key = lambda x: x['Last'])
		with open(fileName, 'w') as output:
			csv_file = csv.DictWriter(output,keys)
			csv_file.writerows(sortlast)
	if col is 'Email':
		sortemail = sorted(shortened, key = lambda x: x['Email'])
		with open(fileName, 'w') as output:
			csv_file = csv.DictWriter(output,keys)
			csv_file.writerows(sortemail)




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

