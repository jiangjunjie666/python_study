# 这次我们想用函数来写计算，并得到结果。让我们看一下一些例子：

# ```python
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# ```

# 要求：

# - 从0（"零"）到9（"九"）的每个数字都必须有一个函数。
# - 必须有一个函数用于以下数学运算：加、减、乘、除。
# - 每个计算都由一个操作和两个数字组成。
# - 最外面的函数代表左边的操作数，最里面的函数代表右边的操作数。
# - 除法应该是整数除法。

def zero(operation=None):
    return 0 if operation is None else operation(0)


def one(operation=None):
    return 1 if operation is None else operation(1)


def two(operation=None):
    return 2 if operation is None else operation(2)


def three(operation=None):
    return 3 if operation is None else operation(3)


def four(operation=None):
    return 4 if operation is None else operation(4)


def five(operation=None):
    return 5 if operation is None else operation(5)


def six(operation=None):
    return 6 if operation is None else operation(6)


def seven(operation=None):
    return 7 if operation is None else operation(7)


def eight(operation=None):
    return 8 if operation is None else operation(8)


def nine(operation=None):
    return 9 if operation is None else operation(9)


def plus(y):
    return lambda x: x + y


def minus(y):
    return lambda x: x - y


def times(y):
    return lambda x: x * y


def divided_by(y):
    return lambda x: x // y


# 示例计算
result1 = seven(times(five()))  # 7 * 5 = 35
result2 = four(plus(nine()))   # 4 + 9 = 13
result3 = eight(minus(three()))  # 8 - 3 = 5
result4 = six(divided_by(two()))  # 6 / 2 = 3

print(result1)  # 输出结果为 35
print(result2)  # 输出结果为 13
print(result3)  # 输出结果为 5
print(result4)  # 输出结果为 3
