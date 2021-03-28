import os
from dotenv import load_dotenv
import re

load_dotenv()

items = os.getenv('ITEMS')
sum = os.getenv('SUM')
order_num = os.getenv('ORDER_NUM')

# 1. Касса перепутала номер в очереди с суммой. Надо поменять эти переменные местами
# меняем местами
sum, order_num = order_num, sum
print(items, sum, order_num)
# 2. Для отчёта боссу, нужно посчитать среднюю стоимость каждой пиццы в заказе
order_num, sum = sum, order_num
print('Привет, Boss! Средняя стоимость пиццы в заказе: ', float(sum) / int(items))
# 3. Если в сумме заказа нету дробей (.00), нужно, чтобы нули не отрисовывались
x = int(float(sum) // 1)
print(x if float(sum) == x else float(sum))
# 4. Если у клиента в номере заказа есть цифра 2, ему положена скидка в 50%
result = re.findall('2', order_num)
if '2' in result:
    print('Поздравляем!!! Скидка 50%. Сумма заказа: ', float(sum) / 2)
else:
    print("Скидка 0%. Сумма заказа: ", float(sum))
# 5. Если кол-во пицц в заказе меньше 2, от номер в очереди нужно сократить на 5