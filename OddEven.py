#ODD-EVEN
items = [x for x in input().split(',')]
print(items)
for i in items:
	if(int(i)%2==0):
		print(i, "EVEN\n")
	else:
		print(i, "ODD\n")



