def decode_bits(bits):
    bits = bits.strip('0')  # 去掉消息开头和结尾的额外0
    # 将消息分割成单词
    words = bits.split('0000000')

    decoded_message = ""

    for word in words:
        # 将单词分割成字符
        characters = word.split('000')
        for character in characters:
            if '1' in character:
                # 将点（1）和划（111）替换为 "." 和 "-"
                character = character.replace('1'*3, '-').replace('1', '.')
            else:
                # 如果无法分辨是点还是划，假设是点
                character = '.'
            decoded_message += character
        decoded_message += ' '  # 在单词之间添加空格

    return decoded_message.strip()


def decode_morse(morseCode):
    words = morseCode.split('   ')  # 根据三个空格切分单词
    decoded_message = ""

    for word in words:
        characters = word.split(' ')  # 根据一个空格切分字符
        for character in characters:
            if character in MORSE_CODE:
                decoded_message += MORSE_CODE[character]
        decoded_message += ' '  # 在单词之间添加空格

    return decoded_message.strip()


# 示例用法
bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000000111110011001100000011"
morse_code = decode_bits(bits)
message = decode_morse(morse_code)
print(message)  # 应返回 "HEY JUDE"
