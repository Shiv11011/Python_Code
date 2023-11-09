'''
	WAP  to print all even number for given range
''' 
start=int(input("Enter the start: "))
end=int(input("Enter the End: "))
for i in range(start, end):
	if i % 2 == 0:
		print(i,end=" ")
print()
