# 喷子正在攻击你的评论区!
# 处理这种情况的一个常见方法是删除喷子评论中的所有元音(字母：a,e,i,o,u)，以消除威胁。
# 你的任务是写一个函数，接收一个字符串并返回一个去除所有元音的新字符串。
# 例如，字符串 "This website is for losers LOL!" 将变成 "Ths wbst s fr lsrs LL!".

# 注意：对于这个Kata来说，y不被认为是元音。

def disemvowel(string_):
    # 创建一个包含所有元音字母的集合
    vowels = set("aeiouAEIOU")

    # 使用列表推导式来构建新字符串，去除元音字母
    result = [char for char in string_ if char not in vowels]

    # 将列表中的字符连接成一个新字符串
    return ''.join(result)


# 测试
input_string = "This website is for losers LOL!"
output_string = disemvowel(input_string)
print(output_string)  # 输出: "Ths wbst s fr lsrs LL!"
