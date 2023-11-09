'''
	1  2  3  4
	1  2  3
	1  2
	1
'''
for i in range(4):
	num=1
	for j in range(4,i,-1):
		print(num,end=" ")
		num+=1
	print()
	
