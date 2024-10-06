import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00

price = INITIAL_PRICE
number_of_days = 0
OUTPUT_FILE = "stock_prices.txt"

# Opening the output file
out_file = open(OUTPUT_FILE, 'w')

# Print the starting price
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate the stock price changes
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1
    # Randomly decide if the price goes up or down
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = -random.uniform(0, MAX_DECREASE)

    # Update the price
    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Closing the file
out_file.close()
