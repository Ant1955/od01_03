# Сначала определяем длину строки
# в цикле половины длины строки проверяем совпадение букв
# если есть несовпадение то это не палиндром
# можно короче но не наглядно s == s[::-1}

def palindrom (message):
    lnf = int(len(message))
    ln = int(lnf/2)
    lnf -= 1
    for i in range (ln):
        if message[i] != message[lnf-i]:
            return False
    return True

print(palindrom('racecar'))
print(palindrom('hello'))

def plndf(s):
    if s == s[::-1]:
        return True
    return False

print(plndf('racecar'))
print(plndf('hello'))