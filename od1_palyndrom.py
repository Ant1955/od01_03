# палиндром это зеркальное совпадение строки
# Сначала определяем длину строки
# в цикле половины длины строки проверяем совпадение букв
# если есть несовпадение то это не палиндром
# можно короче, но не наглядно s == s[::-1}

def palindrom (message):
    lnf = int(len(message))  # длина строки
    ln = int(lnf/2)         # половина, если нечетное то буква в середине одинаковая
    lnf -= 1                # так как счетчик с нуля
    for i in range (ln):
        if message[i] != message[lnf-i]:
            return False        # при первои несовпадении дальше не проверяем
    return True

print(palindrom('racecar'))
print(palindrom('hello'))

def plndf(s):           # спасибо Нине и библиотеке Python
    if s == s[::-1]:
        return True
    return False

print(plndf('racecar'))
print(plndf('hello'))