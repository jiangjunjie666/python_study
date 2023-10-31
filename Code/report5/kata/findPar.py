# 给你一个包含整数的数组（其长度至少为3，但可能非常大）。该数组要么完全由奇数组成，要么完全由偶数组成，
# 除了一个整数N。请写一个方法，以该数组为参数，返回这个 "离群 "的N。


def find_outlier(integers):
    # 分别统计奇数和偶数的个数
    odd_count = 0
    even_count = 0
    last_odd = 0
    last_even = 0

    for num in integers:
        if num % 2 == 0:
            even_count += 1
            last_even = num
        else:
            odd_count += 1
            last_odd = num

        # 如果已经找到两个奇数或两个偶数，那么最后一个不同类型的数就是离群的N
        if even_count >= 2 and odd_count == 1:
            return last_odd
        elif odd_count >= 2 and even_count == 1:
            return last_even

    # 如果没有找到离群的N，那么根据题意返回最后一个元素
    return last_even if even_count == 1 else last_odd


# 测试示例
arr1 = [2, 4, 0, 100, 4, 11, 2602, 36]
print(find_outlier(arr1))  # 输出 11

arr2 = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(arr2))  # 输出 160
