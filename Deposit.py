# 1. Без ежемесячной капитализации за год:

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input('Введите сумму вклада, руб.: '))

deposit = {'ТКБ': money * per_cent['ТКБ'] / 100,
            'СКБ': money * per_cent['СКБ'] / 100,
            'ВТБ': money * per_cent['ВТБ'] / 100,
            'СБЕР': money * per_cent['СБЕР'] / 100}

print(deposit)
print("Максимальная сумма, которую вы можете заработать - ", max(deposit.values()), "руб.")


# 2. Если добавить еще один или несколько банков программа не посчитает депозиты
# (как решить эту задачу?):
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
print("Максимальная сумма, которую вы можете заработать - ", max(deposit), 'руб.')
print('Чудо не получилось ;-)')

# 3. Ежемесячная капитализация и возможность выбрать срок вклада

print(' ')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print('Сейчас вклады с ежемесячной капиттализацией')

money = float(input('Введите сумму вклада, руб.: '))
months = int(input('Введите срок вклада, мес.: '))

deposit_SKB = deposit_TKB = deposit_VTB = deposit_SBER = money

for i in range(months):
    deposit_SKB += deposit_SKB * per_cent['СКБ'] / 12 / 100
    deposit_TKB += deposit_TKB * per_cent['ТКБ'] / 12 / 100
    deposit_VTB += deposit_VTB * per_cent['ВТБ'] / 12 / 100
    deposit_SBER += deposit_SBER * per_cent['СБЕР'] /12 / 100

deposit = (deposit_TKB-money, deposit_SKB-money, deposit_VTB-money, deposit_SBER-money)
print(deposit)
print("Максимальная сумма, которую вы можете заработать - ", round(max(deposit), 2), 'руб.')
