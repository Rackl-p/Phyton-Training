def caesar_decrypt(encrypted_text, shift):

    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            shifted_char = chr((ord(char) - start - shift_amount) % 26 + start)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

encrypted_text = "Jcnnq Ygnv!!ccdd"
shift_amount = 2
decrypted = caesar_decrypt(encrypted_text, shift_amount)
print("Entschlüsselter Text:", decrypted)