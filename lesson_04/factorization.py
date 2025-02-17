# Любое число раскладывается на произведение простых множителей единственным образом –— с точностью до их перестановки.

# Например, число 8 можно представить как 2 × 2 × 2.

# Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта отличаются лишь порядком следования множителей.

# Разложение числа на простые множители называется факторизацией числа.

# Формат ввода
# В единственной строке дано число n (2 ≤ n ≤ 10 в 9 степени), которое нужно факторизовать.

# Формат вывода
# Выведите в порядке неубывания простые множители, на которые раскладывается число n.

def factorizate(n):
    
    return [n]


def test(n, result):
    if factorizate(n) != result:
        print('Ошибка! Ожидали: ', result, ' -  Получили: ', factorizate(n))
    else:
        print('Отлично: ', result, '==', factorizate(n))

test(8, [2, 2, 2])
test(13, [13])
test(100, [2, 2, 5, 5])