def stock_profit(stock: list) -> int:
    gains =[]
    gain = 0
    for i, val in enumerate(stock):
        gains.append(0)
    for i, val in enumerate(stock):
        for j in range(i + 1, len(stock)):
            gain = stock[j] - val
            if gain > gains[i]:
                gains[i] = gain
    return max(gains)


assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0
assert stock_profit([22, 10, 4, 4, 1]) == 0
assert stock_profit([80, 70, 10, 3, 7]) == 4
assert stock_profit([60, 50, 51, 52, 40]) == 2