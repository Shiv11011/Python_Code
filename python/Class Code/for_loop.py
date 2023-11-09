'''
#Code 1:
for i in range(1,5):
	print(i)

#Code 2:
x=int(input("Enter the number"))
y=int(input("Enter the number"))	
for i in range(x,y+1):
	print(i)

#Code 3:

x=int(input("Enter the number"))
y=int(input("Enter the number"))
for i in range(x,y+1):
	if i % 2 == 0:
	    print("{} is Even".format(i))
	else:
	    print("{} is Odd".format(i))
	
#Code 4:
for i in range(1,5):
	print(i,end=" ") #global scope
print(i)
'''
