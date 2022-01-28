def ceasar_cipher(get_text, shift):
	result = " "
	for i in range(0, len(get_text)):
		char = get_text[i]
		if (char.isupper()):
			result += chr((ord(char) + shift - 65) % 26 + 65)
		else:
			result += chr((ord(char) + shift - 97) % 26 + 97)
	return result

def ceasar_decipher(get_text, shift):
	result = " "
	for i in range(0, len(get_text)):
		char = get_text[i]
		if (char.isupper()):
			result += chr((ord(char) + shift - 65) % 26 + 65)
		else:
			result += chr((ord(char) + shift - 97) % 26 + 97)
	return result

while True:
	en_de = int(input("Enter Encrypt/Decrypt option: 0 for encrypt/ 1 for decrypt >>> "))
	if en_de == 0:
		get_text = input("Enter your secret message : ")
		shift = 4
		#print(len(get_text))
		print("Your encrypted text message is : " + ceasar_cipher(get_text, shift))
	elif en_de == 1:
		get_text = input("Enter your secret message : ")
		shift = -4
		#print(len(get_text))
		print("Your encrypted text message is : " + ceasar_decipher(get_text, shift))
	else:
		print("unknown operation")
		break
