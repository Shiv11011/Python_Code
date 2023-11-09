start=int(input("Enter the start of range: "))	#65
end=int(input("Enter the End of range: "))	#91
for i in range(start, end):
	print("The character of ASCII value {} is {}".format(i,chr(i)))
print()
