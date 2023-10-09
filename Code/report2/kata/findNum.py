# 你的任务是找到一个正整数n的最近的平方数
# 例如，如果n=111，那么nearest_sq(n)（nearestSq(n)）等于121，因为111比100（10的平方）更接近121（11的平方）。
# 如果n已经是完全平方（例如n=144，n=81，等等），你需要直接返回n。

import math

def nearest_sq(n):
    # 如果 n 是完全平方数，直接返回 n
    if math.isqrt(n) ** 2 == n:
        return n
    
    # 找到最近的小于 n 的平方数
    low = math.isqrt(n) ** 2
    
    # 找到最近的大于 n 的平方数
    up = (math.isqrt(n) + 1) ** 2

    # 返回距离 n 最近的平方数
    if n - low <= up - n:
        return low
    else:
        return up


n = int(input())
print(nearest_sq(n))