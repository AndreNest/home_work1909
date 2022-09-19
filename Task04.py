# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево. 
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, 
# которая спрашивает ключ, считывает текст и дешифровывает его.






word  = str(input('Введите слово, для шифрования: '))
key = int(input('Введите ключ шифрования: '))

def encryption(word,key):
    crypt_word = ''
    for i,char in enumerate(word):
        crypt_word += chr(ord(char)+ key)
    print(f'Слово "{word}" в зашифрованном виде: "{crypt_word}", ключ шифрования {key} ---> "encryption.txt"' )
    return crypt_word
file = open("encryption.txt", "w", encoding="utf-8")
file.write(encryption(word,key))
file.close()
file = open("encryption.txt", "r", encoding="utf-8")
cryption_word = file.readline()
def decryption(cryption_word, key):
    decrypt = ''
    for j,char in enumerate(cryption_word):
        decrypt += chr(ord(char) - key)
    print(f'"encryption.txt" ---> Слово "{cryption_word}" в расшифрованном виде: "{decrypt}", ключ шифрования {key}')
    return decrypt
decryption(cryption_word, key)




