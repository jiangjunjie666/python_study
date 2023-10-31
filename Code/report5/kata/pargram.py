# pangram是一个至少包含每个字母一次的句子。例如，"The quick brown fox jumps over the lazy dog "这个句子就是一个pangram，
# 因为它至少使用了一次字母A-Z（大小写不相关）。


def is_pangram(sentence):
    # 将句子中的所有字母转换为小写，以便大小写不相关
    sentence = sentence.lower()

    # 创建一个包含所有字母的集合
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    # 遍历句子中的字符，将其添加到一个集合中
    # 一旦集合包含了所有字母，就返回True
    for char in sentence:
        if char.isalpha():
            alphabet.discard(char)
            if not alphabet:
                return True

    # 如果遍历完成后集合为空，则句子是pangram，否则不是
    return not bool(alphabet)


# 测试示例
sentence1 = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence1))  # 输出 True

sentence2 = "Hello, World!"
print(is_pangram(sentence2))  # 输出 False
