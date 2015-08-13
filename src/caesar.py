# caian 12/08/2015

letters = "abcdefghijklmnopqrstuvwxyz"
signals = " .,!?'\"-\\/<>;:~^()"

def encrypt(m, n):
	enc_m = ""
	m_lower = m.lower()
	letter = 0
	for i in range(0, len(m)):
		if m[i] not in signals:
			letter = letters.index(m_lower[i])
			new_letter = (letter + n) % len(letters)
			if m[i].upper() == m[i]:
				enc_m += str(letters[new_letter]).upper()
			else:
				enc_m += str(letters[new_letter])
		else:
			enc_m += str(signals[signals.index(m[i])])
	return enc_m
		
def decrypt(enc_m, n):
	return encrypt(enc_m, -n)

	
console = "> "
def ask():
	return raw_input(console)

def ask_number():
	return int(ask())

def change_shift():
	print "insert a shift number"
	shift = (ask_number() % len(letters))
	print "the new shift number is %d" % shift
	return shift

def cipher_message(shift):
	print "insert the message:"
	m = ask()
	enc_m = encrypt(m, shift)
	print "Encrypted message:\n%s" % enc_m

def decipher_message(shift):
	print "insert the encrypted message:"
	enc_m = ask()
	m = decrypt(enc_m, shift)
	print "Decrypted message:\n%s" % m

def discover():
	print "insert the message:"
	m = ask()
	print "insert the encrypted message:"
	enc_m = ask()
	print "let me think a little..."
	shift_number = 0
	while(m[0].upper() != decrypt(str(enc_m[0]), shift_number).upper()):
		shift_number += 1
	print "Ok! the shift is: %d" % shift_number

options = {
	0 : "exit",
	1 : "insert a shift number",
	2 : "insert a message to cipher",
	3 : "insert a cipher-message to decrypt",
	4 : "discover a shift number"
}

print "This is a simple Caesar cipher."
shift = 0
while(1):
	print "What to do?"
	for i in options:
		print "%d - %s" % (i, options[i])
	option = ask_number()
	if (option < 0 or option > 4):
		print "Chose between 0 ~ 4, plz!"
	elif option == 0:
		break
	elif option == 1:
		shift = change_shift()
	elif option == 2:
		cipher_message(shift)
	elif option == 3:
		decipher_message(shift)
	elif option == 4:
		discover()
print "bye! ;)"
