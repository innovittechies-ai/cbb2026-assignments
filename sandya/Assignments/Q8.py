#The Vanishing Warehouse Stock

n = int(input("Enter number of products: "))

products = {}
violations = []

for i in range(n):
    product_id, quantity_change = input(
        "Enter product_id and quantity_change: "
    ).split()

    quantity_change = int(quantity_change)

    products[product_id] = products.get(product_id, 0) + quantity_change

    if quantity_change < 0:
        violations.append(product_id)

if violations:
    print("Violating product IDs:", violations)
else:
    print("No violations")



