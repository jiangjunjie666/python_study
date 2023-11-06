# 你将得到一个字典数组，代表关于首次报名参加你所组织的编码聚会的开发者的数据。
# 你的任务是返回来自欧洲的JavaScript开发者的数量。
# 例如，给定以下列表：

# ```python
# lst1 = [
#   { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
#   { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
#   { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
#   { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
# ]
# ```

# 你的函数应该返回数字1。
# 如果，没有来自欧洲的JavaScript开发人员，那么你的函数应该返回0。

# 注意：
# 字符串的格式将总是"Europe"和"JavaScript"。
# 所有的数据将始终是有效的和统一的，如上面的例子。

def count_developers(lst):
    count = 0  # 初始化计数器
    for developer in lst:
        if developer['continent'] == 'Europe' and developer['language'] == 'JavaScript':
            count += 1
    return count


lst1 = [
    {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland',
        'continent': 'Europe', 'age': 19, 'language': 'JavaScript'},
    {'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti',
        'continent': 'Oceania', 'age': 28, 'language': 'JavaScript'},
    {'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan',
        'continent': 'Asia', 'age': 35, 'language': 'HTML'},
    {'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan',
        'continent': 'Asia', 'age': 30, 'language': 'CSS'}
]

print(count_developers(lst1))
