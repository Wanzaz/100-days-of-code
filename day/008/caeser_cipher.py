alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
	cipher_text = "" 
	for i in range(0, len(plain_text)):
		position = alphabet.index(plain_text[i])
		cipher_text += alphabet[position + shift_amount] 
	print(f"The encoded text is: {cipher_text}")

def decrypt(cipher_text, shift_amount):
	plain_text = "" 
	for i in range(0, len(cipher_text)):
		position = alphabet.index(cipher_text[i])
		plain_text += alphabet[position - shift_amount] 
	print(f"The decoded text is: {plain_text}")

if direction == "encode":
	encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
	decrypt(cipher_text=text, shift_amount=shift)
else:
	print("Write is right! Try again!")
	
