char = input("Enter a character: ")

if len(char) == 1 and ('a' <= char <= 'z' or 'A' <= char <= '2'): 
	print("() is an alphabet.".format(char))

else:
	 print("() is not an alphabet.".format(char))

