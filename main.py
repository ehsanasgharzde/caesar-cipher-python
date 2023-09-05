alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']

print('Welcome To The Caesar Cipher\n')

def ceaser(text, shift, direction):
    charlist = list(text)
    cryptedtext = ''

    for character in charlist:
        
            if character.isalpha():
                position = alphabet.index(character)

                if direction == 'encode':
                    cryptedposition = position + shift
                
                elif direction == 'decode':
                    cryptedposition = position - shift
                
                cryptedletter = alphabet[cryptedposition]
                cryptedtext += cryptedletter

            else:
                cryptedtext += character
    
    print(f'the {direction}d text is {cryptedtext}')


proceed = 'yes'

while proceed == 'yes':
    
    direction = input('type \'encode\' to encrypt, type \'decode\' to decrypt: \n').lower()
    text = input('what is your message? \n').lower()
    shift = int(input('type the shift number: \n'))
    
    if shift > 26:
        shift = shift % 26

    ceaser(text, shift, direction)
    
    proceed = input("if you want to run again type 'yes', otherwise type 'no': ")
    
print('\nThanks for choosing Ceaser Cipher.\n')