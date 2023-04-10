'''this is a code to decipher a ceaser cipher'''

# get the encrypted text
encrypted_text = "cz sio uly lyuxcha nbcm nbyh sio'py mowwymmzoffs xywixyx cn"

# get the index of the word seperators


# alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

shift = 0
max_shift = 7 # Enter nuber of shifts to perform
decrypted_text = []

for i in range(0,max_shift): # loop through all possible shifts
    shift = i # shift the alphabet
    string = ''
    for letter in encrypted_text: # loop through each letter in the encrypted text
        if letter in alphabet: # if the letter is in the alphabet
            letter_index = alphabet.find(letter) # find the index of the letter
            decrypted_letter = alphabet[(letter_index + shift) % 26] # shift the letter
            # add the decrypted letter to the string
            string += decrypted_letter
        else:
            # add the letter to the string
            string += letter
    decrypted_text.append(string)

# print the decrypted text
length = len(decrypted_text)
majority = length - 1

print('Decryption initialized: ')
for i in range(majority):
    print('Shift num ' + str(i+1) + ': ' + decrypted_text[i])

print('\nDecryption complete:           (Last shift is most likely the correct one)')
print('Shift num ' + str(length) + ': ' + decrypted_text[length - 1])
