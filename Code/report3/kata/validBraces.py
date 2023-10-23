# 写一个函数，接收一串括号，并确定括号的顺序是否有效。如果字符串是有效的，它应该返回True，如果是无效的，它应该返回False。

# "(){}[]" => True
# "([{}])" => True
#  "(}" => False
#  "[(])" => False
# "[({})](]" => False

def valid_braces(string):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in string:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack
    pass


print(valid_braces("(){}[]"))
print(valid_braces("([{}])"))
print(valid_braces("[(])"))
