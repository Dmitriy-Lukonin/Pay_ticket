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
