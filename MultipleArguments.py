#Takes specified number of strings
print("Enter five strings...We'll sort them. :) ")
m = input("Enter a string:  \n")
n = input("Enter another string:  \n")
o = input("Enter another string:  \n")
p = input("Enter another string:  \n")
q = input("Enter another string:  \n")
lst = []
lst.append(m.upper())
lst.append(n)
lst.append(o.upper())
lst.append(p)
lst.append(q.upper())
print("List is : ",lst)
print("Sorted list.... \n")
lst.sort()
print("Sorted List is : ",lst)
#Takes a list or letters
items=[x for x in input()]
print(items)
items.sort()
print(items)
#Takes sequesnce of lines
lines = []
while True:
	s = input("Enter string...\n")
	if s:
		lines.append(s)
	else:
		break;
		
for l in lines:
	print(l)
	
lines.sort()
print(lines)

for sentences in lines:
	print(sentences.upper())