# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

s = input("Введите текст: ")

with open('inp.txt', 'w') as data:
    data.write(s)


def cod_txt(s):
    count = 1
    res = ''
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            res = res + str(count) + s[i]
            count = 1
    if count > 1 or (s[len(s) - 2] != s[-1]):
        res = res + str(count) + s[-1]
    return res


a = cod_txt(s)

with open('inp.txt_1', 'w') as data:
    data.write(''.join(map(str, a)))


def decod_txt(s:str):
        a = ''
        count = 1
        res = ''
        for i in range(len(s)):
            if not s[i].isalpha():
                a += s[i]
            else:
                res = res + s[i]
                a = ''
        return res

t = decod_txt(s)

with open('inp.txt_2', 'w') as data:
    data.write(''.join(map(str, t)))


print(f"Текст после сжатия: {cod_txt(s)}")
print(f"Текст после восстановления: {decod_txt(t)}")