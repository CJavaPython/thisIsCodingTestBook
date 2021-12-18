#500 100 50 10 coin
#least coin using
money = int(input())
count = 0
coin_types=[500,100,50,10]
for coin in coin_types:
    count += money
    money %= coin

