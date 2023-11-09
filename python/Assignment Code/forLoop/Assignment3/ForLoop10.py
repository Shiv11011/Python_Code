start=int(input("Enter the start: "))
end=int(input("Enter the End: "))
product=1
for i in range(start, end+1):
	if i % 2 != 0:
		product*=i
print(product)
