# 如果我们列出所有低于 10 的 3 或 5 倍数的自然数，我们得到 3、5、6 和 9。这些数的总和为 23. 完成一个函数，使其返回小于某个整数的所有是3 或 5 的倍数的数的总和。此外，如果数字为负数，则返回 0。
# 注意：如果一个数同时是3和5的倍数，应该只被算一次。

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
    pass
  

print(solution(10))