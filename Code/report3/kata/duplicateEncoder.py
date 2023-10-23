# 本练习的目的是将一个字符串转换为一个新的字符串，如果新字符串中的每个字符在原字符串中只出现一次，则为"("，如果该字符在原字符串中出现多次，则为")"。在判断一个字符是否是重复的时候，请忽略大写字母。
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

def duplicate_encode(word):
    word = word.lower()
    new_word = ''
    for i in word:
        if word.count(i) == 1:
            new_word += '('
        else:
            new_word += ')'
    return new_word


print(duplicate_encode('din'))
print(duplicate_encode('recede'))
