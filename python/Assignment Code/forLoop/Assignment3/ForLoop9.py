#	 WAP to print the count of all negative number in given range
start=int(input("Enter the start: "))
end=int(input("Enter the End: "))
count=0
for i in range(start, end):
	if i < 0:
		count+=1
	
print(count)
