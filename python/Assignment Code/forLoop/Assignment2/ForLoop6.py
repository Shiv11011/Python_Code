'''
	1 0 1 0 1
	1 0 1 0
	1 0 1 
	1 0
	1
'''
for i in range(5):
	for j in range(5,i,-1):
		if(j%2==0):
			print("0",end=" ")
		else:
			print("1",end=" ")
	print()
	
