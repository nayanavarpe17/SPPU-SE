def merge_sort(orders):
    if len(orders) <= 1:
        return orders

    mid = len(orders) // 2
    left = merge_sort(orders[:mid])
    right = merge_sort(orders[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]['delivery_time'] < right[j]['delivery_time']:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]


# Main program
orders = []

n = int(input("Enter number of orders: "))

for i in range(n):
    oid = input("Enter Order ID: ")
    time = int(input("Enter delivery time: "))
    orders.append({'order_id': oid, 'delivery_time': time})

sorted_orders = merge_sort(orders)

print("\nSorted Orders:")
for order in sorted_orders:
    print(order['order_id'], "->", order['delivery_time']) 
