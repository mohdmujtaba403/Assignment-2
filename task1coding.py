
# encrypting
def encrypt_mytext(text, n, m):

    result = ""

    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                shift = n * m
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            elif 'n' <= char <= 'z':
                shift = n + m
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            else:
                result += char
        elif char.isupper():
          
            if 'A' <= char <= 'M':
                shift = n
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            elif 'N' <= char <= 'Z':
                shift = m ** 2
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += char
        else:
            result += char
    return result
# decrypting
def decrypt_mytext(text, n, m):
    result = ""
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                shift = n * m
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif 'n' <= char <= 'z':
                shift = n + m
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += char
        elif char.isupper():
            if 'A' <= char <= 'M':
                shift = n
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif 'N' <= char <= 'Z':
                shift = m ** 2
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += char
        else:
            result += char
    return result


def check_correctness_verify(original, decrypted):
    return original == decrypted

# reading the raw dataset
with open(r"C:\Users\Dell\Downloads\HIT137 Assignment 2 S1 2025 (4)\raw_text.txt", "r") as file:
    original_text = file.read()

# taking input from user
def take_user():
    n = int(input("User please  value for n: "))
    m = int(input("User please value for m: "))
    return n,m

n,m=take_user()

encrypted_text = encrypt_mytext(original_text, n, m)

with open(r"C:\Users\Dell\Downloads\HIT137 Assignment 2 S1 2025 (4)\decrypted_debug.txt", "w") as file:
    file.write(encrypted_text)

decrypted_text = decrypt_mytext(encrypted_text, n, m)

if check_correctness_verify(original_text, decrypted_text):
    print("Decryption successful!")
else:
    print("Decryption failed!")
    with open(r"C:\Users\Dell\Downloads\HIT137 Assignment 2 S1 2025 (4)\decrypted_debug.txt", "w") as f:
        f.write(decrypted_text)
    print("Saved decrypted output in 'decrypted_debug.txt' file ")

