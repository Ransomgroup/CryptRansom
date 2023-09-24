import string

def generate_cipher_from_keyword(keyword):
    alphabet = string.printable
    unique_chars = ''.join(sorted(set(keyword), key=keyword.index))
    remaining_chars = ''.join(char for char in alphabet if char not in unique_chars)
    cipher = unique_chars + remaining_chars
    return dict(zip(alphabet, cipher))

def encrypt(plaintext, cipher):
    ciphertext = ""
    for char in plaintext:
        if char in cipher:
            ciphertext += cipher[char]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, cipher):
    reverse_cipher = {v: k for k, v in cipher.items()}
    return encrypt(ciphertext, reverse_cipher)

if __name__ == "__main__":
    keyword = ""
    cipher = generate_cipher_from_keyword(keyword)

    print("Cryptogramme:", cipher)

    choice = input("Choisissez l'option : (1) Crypter ou (2) Décrypter : ")

    if choice == "1":
        message = input("Entrez le message à crypter : ")
        encrypted_message = encrypt(message, cipher)
        print("Message crypté :", encrypted_message)
    elif choice == "2":
        message = input("Entrez le message à décrypter : ")
        decrypted_message = decrypt(message, cipher)
        print("Message décrypté :", decrypted_message)
    else:
        print("Option invalide. Veuillez choisir soit '1' pour crypter, soit '2' pour décrypter.")
