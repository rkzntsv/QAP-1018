money = int(input("Сумма, которую вы планируете положить под проценты сроком на один год: "))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

tkb = int((per_cent['ТКБ']) * money / 100)
skb = int((per_cent['СКБ']) * money / 100)
vtb = int((per_cent['ВТБ']) * money / 100)
sber = int((per_cent['СБЕР']) * money / 100)

deposit = [tkb, skb, vtb, sber]

print("Накопленные средства за год вклада в каждом из банков:", deposit)

print("Максимальная сумма, которую вы можете заработать:", max(deposit))