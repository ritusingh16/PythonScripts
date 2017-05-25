n = int(input("Enter a digit\n"))
print("Entered digit is: ", n)
if (n%2 == 0
	and n in range(2,5)
	):
	print("Weird, number is even, but falls in range 2 to 5")
elif (n%2 == 0
	and n in range(6,20)
	):
	print("Not Weird, number is even and falls in range 6 to 20")
elif (n%2 == 0
	and n>20
	):
	print("Weird, number is even and falls is greater than 20")
else:
	print("Weird, the number is odd.")