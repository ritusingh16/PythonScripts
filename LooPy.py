n = int(input("Enter number less than 20, please: \n"))
print("Enterend number is :", n)
if(n<20):
	print("Number is less than 20. Good Boy!!")
	for i in range(0,n):
		print("Square of ", i , "is : " , i*i)
else:
	print("Try Again, mate!! :P")