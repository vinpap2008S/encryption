import string

def enigma_encrypt(message, rotors, reflector):
    message = message.upper()
    encrypted_message = ""
    for char in message:
        if char in string.ascii_uppercase:
            index = (ord(char) - ord('A')) % 26
            for rotor in rotors:
                index = (index + rotor) % 26
            index = (index + reflector) % 26
            for rotor in reversed(rotors):
                index = (index - rotor) % 26
            encrypted_char = chr(index + ord('A'))
            encrypted_message += encrypted_char
            # Поворот роторов после каждого символа
            rotors[0] = (rotors[0] + 1) % 26
            if rotors[0] == 0:
                rotors[1] = (rotors[1] + 1) % 26
                if rotors[1] == 0:
                    rotors[2] = (rotors[2] + 1) % 26
                    if rotors[2] == 0:
                        rotors[3] = (rotors[3] + 1) % 26
                        if rotors[3] == 0:
                            rotors[4] = (rotors[4] + 1) % 26
        else:
            encrypted_message += char
    return encrypted_message

def enigma_decrypt(message, rotors, reflector):
    decrypted_message = ""
    for char in message:
        if char in string.ascii_uppercase:
            index = (ord(char) - ord('A')) % 26
            for rotor in rotors:
                index = (index + rotor) % 26
            index = (index + reflector) % 26
            for rotor in reversed(rotors):
                index = (index - rotor) % 26
            decrypted_char = chr(index + ord('A'))
            decrypted_message += decrypted_char
            # Поворот роторов после каждого символа
            rotors[0] = (rotors[0] + 1) % 26
            if rotors[0] == 0:
                rotors[1] = (rotors[1] + 1) % 26
                if rotors[1] == 0:
                    rotors[2] = (rotors[2] + 1) % 26
                    if rotors[2] == 0:
                        rotors[3] = (rotors[3] + 1) % 26
                        if rotors[3] == 0:
                            rotors[4] = (rotors[4] + 1) % 26
        else:
            decrypted_message += char
    return decrypted_message

# Пример использования:
rotors = [1, 2, 3, 4, 5]  # Позиции роторов (0-25)
reflector = 6       # Позиция рефлектора (0-25)

alpha = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = input().strip()
res = ''
for c in s:
    res += alpha[(alpha.index(c) + n) % len(alpha)]
print('Result: "' + res + '"')

message = res
encrypted_message = enigma_encrypt(message, rotors, reflector)
print("Зашифрованное сообщение:", encrypted_message)



decrypted_message = enigma_decrypt(encrypted_message, rotors, -reflector)
print("Расшифрованное сообщение:", decrypted_message)

decrypted_message = decrypted_message.lower()
res1 = ""
for c in decrypted_message:
    res1 += alpha[(alpha.index(c) - n) % len(alpha)]
print(res1)
