# 圣诞老人要来镇上了，他需要你帮助找出谁是淘气的或善良的。你将会得到一整年的JSON数据，按照这个格式：

# {
#     January: {
#         '1': 'Naughty','2': 'Naughty', ..., '31': 'Nice'
#     },
#     February: {
#         '1': 'Nice','2': 'Naughty', ..., '28': 'Nice'
#     },
#     ...
#     December: {
#         '1': 'Nice','2': 'Nice', ..., '31': 'Naughty'
#     }
# }

# 你的函数应该返回 "Naughty!"或 "Nice!"，这取决于在某一年发生的总次数（以较大者为准）。如果两者相等，则返回 "Nice！"。

def naughty_or_nice(data):
    naughty_count = 0
    nice_count = 0
    for month in data:
        for day in data[month]:
            behavior = data[month][day]  # 获取每天的行为
            if behavior == 'Naughty':
                naughty_count += 1
            elif behavior == "Nice":
                nice_count += 1

    if (naughty_count > nice_count):
        return 'Naughty!'
    elif (naughty_count < nice_count):
        return 'Nice!'
    else:
        return 'Nice!'


# 用你提供的JSON数据调用这个函数
santa_data = {
    "January": {
        '1': 'Naughty', '2': 'Naughty', '31': 'Nice'
    },
    "February": {
        '1': 'Nice', '2': 'Naughty', '28': 'Nice'
    },
    "December": {
        '1': 'Nice', '2': 'Nice', '31': 'Naughty'
    }
}

result = naughty_or_nice(santa_data)
print(result)
