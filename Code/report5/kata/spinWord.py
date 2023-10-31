# 编写一个函数，接收一个或多个单词的字符串，并返回相同的字符串，但所有5个或更多的字母单词都是相反的（就像这个Kata的名字一样）。
# 传入的字符串将只由字母和空格组成。只有当出现一个以上的单词时，才会包括空格。

def spinWords(str):
    words = str.split(' ')
    new_words = []
    for word in words:
        if len(word) >= 5:
            new_words.append(word[::-1])
        else:
            new_words.append(word)
    return ' '.join(new_words)


print(spinWords("Hey fellow warriors"))
print(spinWords("This is a test"))
print(spinWords("This is another test"))
