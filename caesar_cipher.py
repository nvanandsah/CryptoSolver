def solveCaesar(shift,text):
	keyL = 'abcdefghijklmnopqrstuvwxyz'
	keyU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	value = ''
	for t in text:
		indexL = keyL.find(t)
		indexU = keyU.find(t)
		if(indexL != -1):
				value = value + keyL[indexL-shift]
		elif(indexU != -1):
				value = value + keyU[indexU-shift]
		else:
			value = value + t
	return value

Cipher_Text = '''Slnpzshabylzohssthrluvshdylzwljapunhulzahispzotluavmylspnpvuvywyvopipapunaolmylllelyjpz
laolylvmvyhiypknpunaolmyllkvtvmzwlljovyvmaolwylzzvyaolypnoavmaolwlvwslwlhjlhisfavhzz
ltislhukavwlapapvuaolnvclyutluamvyhylkylzzvmnyplchujlz nhtl vm aoyvulz zlhzvu lpnoa
zwvpslyz qvu zuvd huk khlulyfz ahynhyflu av rpss lhjo vaoly'''
notsolved = True
shift = 0
while  notsolved==True:
	print(" Trying Shift "+str(shift))
	result = solveCaesar(shift,Cipher_Text)
	print(result)
	temp = input("Does it make sense ? [(Y)es/(N)o]")
	temp = temp.lower()
	temp = temp[0]
	if(temp == 'y'):
		notsolved = False
	elif (temp == 'n'):
		shift = shift + 1
	else:
		print("Enter valid option")
print(" \nThe plain text was shift by "+str(shift)+" characters")
print("\n Found plain text : \n" + result)
