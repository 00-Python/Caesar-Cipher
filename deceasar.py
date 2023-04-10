'''this is a code to crack a ceaser cipher'''

# get the encrypted text
encrypted_text = "cz sio uly lyuxcha nbcm nbyh sippy mowwymmzoffs xywixyx cn"

# get the index of the word seperators
space_index = []
for i in range(len(encrypted_text)):
    if encrypted_text[i] == " ":
        space_index.append(i)

# alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

shift = 0
max_shift = 7
decrypted_text = []

for i in range(1,max_shift): # loop through all possible shifts
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
print(decrypted_text)
