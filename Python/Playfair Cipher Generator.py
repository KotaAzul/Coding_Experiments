def find_in_sublists(lst, value):
    for sub_i, sublist in enumerate(lst):
        try:
            return (sub_i, sublist.index(value))
        except ValueError:
            pass


##First we have to generate the cipher keygrid with our key phrase
def make_keygrid(key, letter):
	key=key.upper()
	keystring = ""
	alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	## The keystring first beings with the input str variable
	## Afterwards, it appends the other letters of the alphabet to the string, 
	## except for letter which already appeared in the input and a chosen letter to ignore.
	## The ignored letter is usually Q by default, as Q is not used frequently in english.
	## You can choose to ignore any one letter, so long as it does not need to appear in the encrypted text.
	for i in key:
		if i in keystring:
			pass
		else:
			keystring+=i
	for i in alphabet:
		if i in keystring or i == letter:
			pass
		else:
			keystring+=i

	##print (keystring)
	##print (len(keystring))
## Now that we have our keystring, let's make it in to a 5x5 grid
	keygrid = [""]*5
	for i in range(5):
		keygrid[i]=[""]*5

	keygrid[0]=keystring[:5]
	keygrid[1]=keystring[5:10]
	keygrid[2]=keystring[10:15]
	keygrid[3]=keystring[15:20]
	keygrid[4]=keystring[20:]

	return keygrid

def playfair_cipher(key, letter, message, intent):
	key=key.upper()
	letter=letter.upper()
	message=message.replace(" ", "")
	message=message.upper()
	intent=intent.upper()
	cipher_message=""
	
	keygrid = make_keygrid(key, letter)
	print(keygrid)

##In a playfair cipher you can only encode digraphs of two letters. If the message has an odd number of letters, simply add a Z on the end to give the last letter a partner 

	if len(message)%2 != 0:
		message+="Z"

	paircount=0

## Now we iterate over the message taking two letters at a time to encode them. In a playfair cipher, encoding digraphs follows 3 rules:
	# If the letters are in the same row of the grid, you simply shift each letter one space to the left
	# If the letters are in the same column, each letter gets shifted down one space
	# If neither of the above are true, form a rectangle around the two letters and shift each letter to the space which is in the opposite horizontal corner from it

	while paircount <= len(message)-2:

		pair_code=""

		letpair=message[paircount:paircount+2]
		paircount+=2

		
		letPairOneCoords=list(find_in_sublists(keygrid, letpair[0]))
		# print(letpair[0])
		# print(letPairOneCoords)


		letPairTwoCoords=list(find_in_sublists(keygrid, letpair[1]))
		# print(letpair[1])
		# print(letPairTwoCoords)
		if intent == "E":
			if letPairOneCoords[0] == letPairTwoCoords[0]:
				letPairOneCoords[1] = letPairOneCoords[1]+1
				letPairTwoCoords[1] = letPairTwoCoords[1]+1

				if letPairOneCoords[1] > 4:
					letPairOneCoords[1] = 0
				if letPairTwoCoords[1] > 4:
					letPairTwoCoords[1] = 0

			elif letPairOneCoords[1] == letPairTwoCoords[1]:
				letPairOneCoords[0] = letPairOneCoords[0]+1
				letPairTwoCoords[0] = letPairTwoCoords[0]+1

				if letPairOneCoords[0] > 4:
					letPairOneCoords[0] = 0
				if letPairTwoCoords[0] > 4:
					letPairTwoCoords[0] = 0

			else:
				holderOne=letPairOneCoords[1]
				holderTwo=letPairTwoCoords[1]
				letPairOneCoords[1] = holderTwo
				letPairTwoCoords[1] = holderOne

			pair_code=keygrid[letPairOneCoords[0]][letPairOneCoords[1]]+keygrid[letPairTwoCoords[0]][letPairTwoCoords[1]]
			cipher_message+=pair_code
## If the user would like to decrypt a ciphered message, given that they know the keyword and missing letter, the inverse of the above rules are performed
## with the exception of rule 3, as that is not a strictly directional change 
		elif intent == "D":
			if letPairOneCoords[0] == letPairTwoCoords[0]:
				letPairOneCoords[1] = letPairOneCoords[1]-1
				letPairTwoCoords[1] = letPairTwoCoords[1]-1

				if letPairOneCoords[1] > 4:
					letPairOneCoords[1] = 0
				if letPairTwoCoords[1] > 4:
					letPairTwoCoords[1] = 0

			elif letPairOneCoords[1] == letPairTwoCoords[1]:
				letPairOneCoords[0] = letPairOneCoords[0]-1
				letPairTwoCoords[0] = letPairTwoCoords[0]-1

				if letPairOneCoords[0] < 0:
					letPairOneCoords[0] = 4
				if letPairTwoCoords[0] < 0:
					letPairTwoCoords[0] = 4

			else:
				holderOne=letPairOneCoords[1]
				holderTwo=letPairTwoCoords[1]
				letPairOneCoords[1] = holderTwo
				letPairTwoCoords[1] = holderOne

			pair_code=keygrid[letPairOneCoords[0]][letPairOneCoords[1]]+keygrid[letPairTwoCoords[0]][letPairTwoCoords[1]]
			cipher_message+=pair_code

	print(cipher_message)


playfair_cipher("fox","Q","JCWKBLNMYXYGFZNNKWAIZU", "d")
