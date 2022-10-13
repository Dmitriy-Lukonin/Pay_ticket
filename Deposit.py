# 1. Без ежемесячной капитализации за год:

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input('Введите сумму вклада, руб.: '))

deposit = {'ТКБ': money * per_cent['ТКБ'] / 100,
            'СКБ': money * per_cent['СКБ'] / 100,
            'ВТБ': money * per_cent['ВТБ'] / 100,
            'СБЕР': money * per_cent['СБЕР'] / 100}

print(deposit)
print("Максимальная сумма, которую вы можете заработать - ", max(deposit.values()), "руб.")


# 2. Если добавить еще один или несколько банков программа не посчитает депозиты:
# Если ввести 100000.00 программа не работет - float в помощь.

print(' ')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print('Добавили банк ЧУДО с процентной ставкой 12.2% годовых')
per_cent['ЧУДО'] = 12.2

money = int(input('Введите сумму вклада, руб.: '))

deposit_TKB = money * per_cent['ТКБ'] / 100
deposit_SKB = money * per_cent['СКБ'] / 100
deposit_VTB = money * per_cent['ВТБ'] / 100
deposit_SBER = money * per_cent['СБЕР'] / 100

# Как можно взять из словаря ключи 'ТКБ', 'ЧУДО' и др. и назначить каждому ключу переменную
# с помощью кода Python?

deposit = (deposit_TKB, deposit_SKB, deposit_VTB, deposit_SBER)
print(deposit)
print("Максимальная сумма, которую вы можете заработать - ", max(deposit))
print('Чудо не получилось ;-)')