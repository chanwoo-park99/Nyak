yo_price = 1800
yo_qty = 4
milk_price = 1500
milk_qty = 2
ball_price = 1000
ball_qty = 3

yo_sales = yo_price * yo_qty
milk_sales = milk_price * milk_qty
ball_sales = ball_price * ball_qty

total_sales = yo_sales + milk_sales + ball_sales
total_qty = yo_qty + milk_qty + ball_qty

print("드링킹 요구르트 매출액: " + str(yo_sales))
print("딸기 우유 매출액: " + str(milk_sales))
print("홈런공 매출액: " + str(ball_sales))
print("-" * 20)
print("총 매출액: " + str(total_sales))
print("총 판매량: " + str(total_qty))
