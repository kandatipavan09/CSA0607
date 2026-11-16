"""KartIQ Module 1: Stable Merge Sort for order consolidation."""
from dataclasses import dataclass

@dataclass
class Order:
    timestamp: int
    order_id: str

def merge_sort_orders(orders):
    """Stable merge sort. Equal timestamps are taken from the left run first."""
    if len(orders) <= 1:
        return orders[:]
    mid = len(orders) // 2
    left = merge_sort_orders(orders[:mid])
    right = merge_sort_orders(orders[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].timestamp <= right[j].timestamp:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def main():
    orders = [Order(105,"O1"), Order(102,"O2"), Order(105,"O3"),
              Order(101,"O4"), Order(102,"O5"), Order(103,"O6")]
    print("KARTIQ MODULE 1 - STABLE MERGE SORT")
    print("Input:", [(o.timestamp,o.order_id) for o in orders])
    result = merge_sort_orders(orders)
    print("Sorted:", [(o.timestamp,o.order_id) for o in result])
    print("Stable for timestamp 102:", [o.order_id for o in result if o.timestamp==102] == ["O2","O5"])
    print("Stable for timestamp 105:", [o.order_id for o in result if o.timestamp==105] == ["O1","O3"])

if __name__ == "__main__":
    main()
