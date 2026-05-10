import csv
import argparse

waterRegions = []
waterCountries = []
COUNTRYFILENAME = "Data/Water_country.csv"
REGIONFILENAME = "Data/Water_region.csv"

def main():
	""" When you run this program, you'll pass in arguments like so:
	
		python3 command_line.py --location location/region --year year

		Both arguments are optional, but you must have at least one.
	"""
	cla_parser = setUpParser()
	args = cla_parser.parse_args()

	loadData()
	result = getData(args.location, args.year)

	printData(result)
	
	
	
def getData(location, year) -> list: 
	"""This function gets the data requested by the user from `waterRegions` and `waterCounties` and returns it as a list."""
	result = []
	
	
	# if user specified no arguments, return an error.
	if (location == None and year == None):
		return "Error: No arguments provided. Please use flags -l for location and -y for year."

	# if user does not input a year and only a location, return data for all years.
	elif (year == None and location != None):
		for row in waterCountries:
			if row[0] == location:
				result.append(row)
		for row in waterRegions:
			if row[0] == location:
				result.append(row)

	# if user has input a year, check if it is in the acceptable range.
	elif (2000 > int(year) or int(year) > 2024):
		return "Year outside range, please specify a year in the range 2000-2024"

	# if user inputs a year and a location, it will return the associated data.
	elif (location != None and year != None):
		for row in waterRegions:
			if (row[0] == location and row[1] == year):
				result.append(row)
		for row in waterCountries:
			if (row[0] == location and row[1] == year):
				result.append(row)

	# if user does not input a location and only a year, it will return all data for countries and regions for that year
	elif (location == None and year != None): 
		for row in waterRegions: 
			if row[1] == year: 
				result.append(row)
		for row in waterCountries: 
			if row[1] == year: 
				result.append(row)

	# if nothing was found, throw an error.
	if result == []:
		return "Error: Country or region not found, please try again."

	return result

def printData(data):
	"""Print data in a more organized manner, as well as column headers."""
	print("Retrieved Data, with location, year, and associated data:\n\nColumn Headers:")

	if (len(data[0]) == 48):
		print(waterCountries[2], end="")
		for row in data:
			print("\n")
			for col in row:
				print(col + "\t", end="")
	elif (len(data[0]) == 44):
		print(waterRegions[2], end="")
		for row in data:
			print("\n")
			for col in row:
				print(col + "\t", end="")

def setUpParser():
	"""Defines the command line arguments we'll accept"""
	parser = argparse.ArgumentParser()
	parser.add_argument('-l', '--location') # what country or region do you want info on. If no country is specified return all countries
	parser.add_argument('-y', '--year') # what year to retrieve data for. If no year is specified return all years
	return parser

def loadData():
	"""Loads in data from CSV files and stores it in `waterCountries` and `waterRegions`"""
	with open(COUNTRYFILENAME, newline='') as datafile:
		csv_file = csv.reader(datafile)
		for row in csv_file:
			waterCountries.append(row)

	with open(REGIONFILENAME, newline='') as datafile:
		csv_file = csv.reader(datafile)
		for row in csv_file:
			waterRegions.append(row)

	
if __name__ == '__main__':
	main()