#Code1 :
playerList=["Rohit","Shubhman","Virat","Iyer","KLRahul"]
playerName=input("Enter the player Name :")
for player in playerList:
    if player == playerName:
        print(playerName,"present in list")
        break
else:
	print(playerName,"not present in list")
