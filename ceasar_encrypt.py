def caesar_encrypt(text, shift):

    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
                shifted_char = chr((ord(char) - start + shift_amount) % 26 + start)
                encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

text_to_encrypt = "Jcnnq Ygnv!!ccdd"
shift_amount = 2
encrypted = caesar_encrypt(text_to_encrypt, shift_amount)
print("Verschlüsselter Text:", encrypted)