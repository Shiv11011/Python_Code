#Program to check given character is vowel consonant or a special character
char = input("Enter the character: ")
if len(char) == 1 and (char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
	print("Vowel")
else:
	print("Character is consonant or Special Character") 
