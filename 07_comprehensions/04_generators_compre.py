daily_sales = [4 , 7, 15, 3 , 20, 2,11]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)