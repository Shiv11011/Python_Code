'''
	1
	3 2
	6 5 4
       10 9 8 7
'''
for i in range(1, 4):
    num = i
    for j in range(i, 0, -1):
        print(num, end=" ")
        num += 1
    print()
