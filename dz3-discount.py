from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-10-25
print(type(today))  # <class 'datetime.date'>

time = datetime.now()  # 2023-10-25 09:32:46.170956
print(time)
print(type(time))  # <class 'datetime.datetime'>

# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomm = today + timedelta(days=1)
print(tomm)
print(type(tomm))  # 2023-10-26

print(time.hour)
print(today.day)

formated_date = datetime.now().strftime('%d/%m/%Y')
print(formated_date)  # 25/10/2023

formated_time = datetime.now().strftime("%H:%M")
print(formated_time)  # 09:44
print(formated_time.removeprefix("0"))  # 9:49

formated_time2 = datetime.now().strftime("%I:%M %p")  # 09:47 AM
print(formated_time2)

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tomm, 'price': 80.0},
    {'sku': 3, 'exp_date': today, 'price': 50},
    {'sku': 4, 'exp_date': today, 'price': 250.0},
]

# print(products)

for product in products:
    # print(product)
    if product['exp_date'] != today:
        continue  # pętla kończy działanie i bierze kolejny element z listy
    # print(f"{product['exp_date']} : jadę dalej")
    product['price'] *= 0.8  # price = price * 0.8
    print(f"""
    Price for sku = {product['sku']}
    is now {product['price']}""")
# 2023-10-25
# <class 'datetime.date'>
# 2023-10-25 10:10:41.140845
# <class 'datetime.datetime'>
# 2023-10-26
# <class 'datetime.date'>
# 10
# 25
# 25/10/2023
# 10:10
# 10:10
# 10:10 AM
#
#     Price for sku = 1
#     is now 80.0
#
#     Price for sku = 3
#     is now 40.0
#
#     Price for sku = 4
#     is now 200.0
