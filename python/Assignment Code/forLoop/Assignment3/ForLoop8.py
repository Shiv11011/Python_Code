#	WAP to print the number divisible by 3 and 5 in given range
start=int(input("Enter the start: "))
end=int(input("Enter the End: "))
for i in range(start, end):
	if i % 3 ==0 and i % 5 == 0:
		print(i,end=" ")
print()
