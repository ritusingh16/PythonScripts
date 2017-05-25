def is_leap(year):
	leap = "Not leap year"
	if(year%400==0):
		leap = "Year is leap"
	elif year % 4 == 0 and year % 100 !=0:
		leap = "Year is leap"
		
	return leap
	
year = int(input("Enter the year: \n"))
print(is_leap(year))