alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type encode to encrypt, type decode to decrypt:\n").lower()
shift = int(input("Type the shift number:\n"))
word = input("Enter the word:\n").lower().strip()

def encrypt(text, shift):
    encode = []
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position + shift) % 26
            encode.append(alphabet[new_position])
        else:
            encode.append(i)  # keeps spaces/symbols unchanged
    return "".join(encode)

def decrypt(text, shift):
    decode = []
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position - shift) % 26
            decode.append(alphabet[new_position])
        else:
            decode.append(i)
    return "".join(decode)

if direction == "encode":
    result = encrypt(word, shift)
    print("Encrypted text:", result)

elif direction == "decode":
    result = decrypt(word, shift)
    print("Decrypted text:", result)

else:
    print("Invalid choice! Type 'encrypt' or 'decode'.")