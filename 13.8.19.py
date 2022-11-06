number_of_tickets = int(input("Сколько билетов вы хотите приобрести на мероприятие? "))

final_price = 0

price_free = 0
price_medium = 990
price_full = 1390

for i in range(number_of_tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        final_price += price_free
    elif 18 <= age < 25:
        final_price += price_medium
    else:
        final_price += price_full

if number_of_tickets > 3:
    final_price -= final_price * 10 // 100

print(final_price)


