#	WAP to print the number between 1 to 100 which are divisible by 7 but not by 3
for i in range(1,101):
	if i % 7 ==0 and i % 3 != 0:
		print(i,end =" ")
print()
