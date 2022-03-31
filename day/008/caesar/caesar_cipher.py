import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
	end_text = "" 
	if cipher_direction == "decode":
		shift_amount *= -1
	for i in range(0, len(start_text)):
		if start_text[i] >= 'a' and start_text[i] <= 'z':
			position = alphabet.index(start_text[i])
			end_text += alphabet[position + shift_amount] 
		else:
			end_text += start_text[i];
	print(f"The {cipher_direction}d text is: {end_text}")

print(art.logo)

answer = "yes" 
while answer == "yes":
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	if shift >= 26:
		print("Shift has to be smaller than 26")
		exit()

	caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
	answer = input("Type 'yes' if you want to go again. Otherwise type 'no': ")

print("Goodbye")
