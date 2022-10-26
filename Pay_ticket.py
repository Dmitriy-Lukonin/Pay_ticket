# ЗАДАНИЕ 13.8.19

# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов.
# Программа должна работать следующим образом:

# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.

# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается
# стоимость:

# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.

# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек
# на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.


all_price = 0
ticket_number = int(input('Сколько билетов Вы хотите приобрести на мероприятие?: '))

for i in range(ticket_number):
    age_for_ticket = int(input(f'Укажите возраст участника № {i+1}: '))

    if age_for_ticket < 18:
        continue
    elif 18 <= age_for_ticket < 25:
        all_price += 990
    else:
        all_price += 1390

if ticket_number > 3 and all_price != 0:
    all_price = all_price * 0.9
    print(f'Сумма к оплате с учетом скидки 10%: {all_price} руб.')
else:
     print(f'Сумма к оплате: {all_price} руб.')

# 4 участника в возрасте 17, 18, 25 , 40 лет.
# Сумма к оплате с учетом скидки 3393.0 руб.