
import csv

portfolio = []

print("===== STOCK PORTFOLIO TRACKER =====")

# Validate number of stocks
while True:
    try:
        n = int(input("How many stocks do you want to add? "))

        if n <= 0:
            print("Enter a number greater than zero.")
        else:
            break

    except ValueError:
        print("Please enter a valid whole number.")

# Enter stock details
for i in range(n):
    print("\nStock", i + 1)

    name = input("Enter stock name: ").strip()

    while not name:
        print("Stock name cannot be empty.")
        name = input("Enter stock name: ").strip()

    while True:
        try:
            quantity = int(input("Enter quantity of shares: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
            else:
                break

        except ValueError:
            print("Enter a valid whole number.")

    while True:
        try:
            price = float(input("Enter purchase price per share: ₹"))

            if price <= 0:
                print("Price must be greater than zero.")
            else:
                break

        except ValueError:
            print("Enter a valid price.")

    investment = quantity * price

    stock = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    }

    portfolio.append(stock)

# Display portfolio
print("\n===== PORTFOLIO SUMMARY =====")

total_investment = 0

for stock in portfolio:
    print("\nStock:", stock["name"])
    print("Quantity:", stock["quantity"])
    print("Price per share: ₹", stock["price"])
    print("Investment: ₹", stock["investment"])

    total_investment += stock["investment"]

print("\nTotal Investment: ₹", round(total_investment, 2))

# Save portfolio to CSV
with open("portfolio.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Stock Name",
        "Quantity",
        "Price Per Share",
        "Total Investment"
    ])

    for stock in portfolio:
        writer.writerow([
            stock["name"],
            stock["quantity"],
            stock["price"],
            round(stock["investment"], 2)
        ])

print("\nPortfolio saved successfully to portfolio.csv")
