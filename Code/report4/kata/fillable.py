def fillable(stock, merch, n):
    if merch in stock and stock[merch] >= n:
        return True
    else:
        return False


stock = {
    'item1': 10,
    'item2': 5,
    'item3': 0
}

print(fillable(stock, 'item1', 5))  # 应返回 True
print(fillable(stock, 'item2', 7))  # 应返回 False
print(fillable(stock, 'item3', 1))  # 应返回 False
