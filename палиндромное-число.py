print('Давайте проверим, является ли число палиндромом!')
a = list(input('Введите любое число:'))

b = a[::-1]

if a == b:
    print('Кайф, число является палиндромом')
else:
    print('Это обыкновенное число')
