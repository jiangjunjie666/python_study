# 您将获得一个对象序列，表示已注册参加您组织的下一个编程聚会的开发人员的数据。

# 您的任务是返回一个序列，其中包括最年长的开发人员。如果有多个开发人员年龄相同，则将他们按照在原始输入数组中出现的顺序列出。

# 例如，给定以下输入数组：

# ```python
# list1 = [
#   { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
#   { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
#   { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
#   { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
# ]
# ```

# 您的程序应该返回如下结果：

# ```python
# [
#   { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
#   { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
# ]
# ```


def find_senior(lst):
    max_age = -1  # 初始的最大年龄
    senior_developers = []

    for developer in lst:
        if developer['age'] > max_age:
            max_age = developer['age']
            senior_developers = [developer]
        elif developer['age'] == max_age:
            senior_developers.append(developer)

    return senior_developers


# 示例输入数据
list1 = [
    {'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco',
        'continent': 'Europe', 'age': 49, 'language': 'PHP'},
    {'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia',
        'continent': 'Asia', 'age': 38, 'language': 'Python'},
    {'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania',
        'continent': 'Europe', 'age': 19, 'language': 'Python'},
    {'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan',
        'continent': 'Asia', 'age': 49, 'language': 'PHP'},
]

result = find_senior(list1)
print(result)
