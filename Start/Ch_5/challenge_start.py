# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

# process each order
for order in test_orders:
    print("--------------")
    order_total = 0
    for item in order:
        match item:
            # use literal strings to make sure we match accepted garments
            case "shirt" | "pants" | "jacket" | "dress" as garment, size, starch, sameday:
                order_total += 12.95
                if starch:
                    order_total += 2.00
                if sameday:
                    order_total += 10.00
                print(f"Dry Clean:({size}) {garment}", "Starched" if starch else "",
                      "same-day" if sameday else "")
            case desc, weight:
                print(f"Wash/Fold: {desc}, weight: {weight}")
                subtotal = weight * 4.95
                if weight > 15: # 10 percent off if more than 15 pounds
                    subtotal *= 0.9
                order_total += subtotal
            case item, True, size:
                print(f"Blanket: ({size}) {item} Dry clean")
                order_total += 25
            case item, False, size:
                print(f"Blanket: ({size}) {item}")
                order_total += 25
            case _:
                print("unknown, could not process order")
    print(f"Order total: {order_total:.2f}")
    print("--------------")