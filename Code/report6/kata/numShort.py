# 在这个kata中，我们将创建一个函数，它返回另一个缩短长数字的函数。给定一个初始值数组替换给定基数的 X 次方。如果返回函数的输入不是数字字符串，则应将输入本身作为字符串返回。

# 例子：

# ```python
# filter1 = shorten_number(['','k','m'],1000)
# filter1('234324') == '234k'
# filter1('98234324') == '98m'
# filter1([1,2,3]) == '[1,2,3]'
# filter2 = shorten_number(['B','KB','MB','GB'],1024)
# filter2('32') == '32B'
# filter2('2100') == '2KB';
# filter2('pippi') == 'pippi'
# ```


def shorten_number(suffixes, base):
    def inner(input_value):
        if isinstance(input_value, int):
            num = input_value
        elif isinstance(input_value, str):
            try:
                num = int(input_value)
            except ValueError:
                return str(input_value)
        else:
            return str(input_value)

        for i in range(len(suffixes) - 1, -1, -1):
            if num >= (base ** i):
                return str(num // (base ** i)) + suffixes[i]
        return str(input_value)
    return inner


# 示例用法
filter1 = shorten_number(['', 'k', 'm'], 1000)
print(filter1('234324'))     # 输出 '234k'
print(filter1('98234324'))   # 输出 '98m'
print(filter1([1, 2, 3]))    # 输出 '[1,2,3]'

filter2 = shorten_number(['B', 'KB', 'MB', 'GB'], 1024)
print(filter2('32'))         # 输出 '32B'
print(filter2('2100'))       # 输出 '2KB'
print(filter2('pippi'))      # 输出 'pippi'
