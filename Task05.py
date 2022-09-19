word_start  = input('Введите текст, для шифрования: ')
file1 = open("coding5.txt", "r+", encoding="utf-8")
file2 = open("decoding5.txt", "r+", encoding="utf-8")
def coding(word):
    count = 1
    res = ''
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            count += 1
        else:
            res = res + str(count) + word[i]
            count = 1
    if count > 1 or (word[len(word)-2] != word[-1]):
        res = res + str(count) + word[-1]
    return res

def decoding(word):
    number = ''
    res = ''
    for i in range(len(word)):
        if not word[i].isalpha():
            number += word[i]
        else:
            res = res + word[i] * int(number)
            number = ''
    return res


file1 = open("coding5.txt", "r+", encoding="utf-8")
file2 = open("decoding5.txt", "r+", encoding="utf-8")
file1.write(coding(word_start))
print(f'Текст после шифрования: {coding(word_start)}')
print(f"Текст после дешефрования: {decoding(coding(word_start))}")
file2.write(decoding(coding(word_start)))
file1.close
file2.close()
