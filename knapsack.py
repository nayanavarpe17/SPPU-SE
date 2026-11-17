profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

items = sorted(zip(profits, weights),
               key=lambda x: x[0]/x[1], reverse=True)

total = 0

for p, w in items:
    if capacity >= w:
        total += p
        capacity -= w
    else:
        total += p * capacity / w
        break

print("Maximum Profit =", total)
