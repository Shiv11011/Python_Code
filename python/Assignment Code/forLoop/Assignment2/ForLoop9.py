'''
	E F G H I
	D E F G
	C D E
	B C
	A
'''
num=69
x=5
for i in range(5):
	for j in range(5,i,-1):
		print(chr(num),end=" ")
		num+=1
	num-=x+1
	x-=1
	print()
	
