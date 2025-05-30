def area(a, b):
    return a * b


def count_order_material(order):
    total = 0
    for batch in order:
        carper_area = area(batch["width"], batch["height"])
        total_material = carper_area * batch["amount"]
        total += total_material
    return total


def print_results(order):
    total_material = count_order_material(order)
    print(f"Total material needed for order is {total_material} cm2")

order = [
    {
        "size": "small",
        "width": 30,
        "height": 20,
        "amount": 27
     },
    {
        "size": "medium",
        "width": 50,
        "height": 40,
        "amount": 34
    }
]

print_results(order)