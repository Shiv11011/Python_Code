'''
	WAP to print sum of all numbers in given range
'''
start=int(input("Enter the start: "))
end=int(input("Enter the End: "))
sum=0
for i in range(start,end):
	sum+=i
print(sum)
