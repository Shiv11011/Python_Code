#	WAP to print ASCII w=value of all character in the given character range
start=input("Enter the start: ")
end=input("Enter the End: ")
for i in range(ord(start), ord(end)+1):
	print("ASCII value of {} is {}".format(chr(i),i))
print()
