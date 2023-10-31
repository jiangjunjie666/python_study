import re

# 预加载的莫尔斯码表
morse_code_dict = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z", "-----": "0", ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8",
    "----.": "9", ".-.-.-": ".", "--..--": ",", "..--..": "?",
    ".----.": "'", "-.-.--": "!", "-..-.": "/", "-.--.": "(", "-.--.-": ")",
    ".-...": "&", "---...": ":", "-.-.-.": ";", "-...-": "=", ".-.-.": "+",
    "-....-": "-", ".-..-.": "_", ".-..-.": '"', "...-..-": "$", ".--.-.": "@"
}


def decodeBits(bits):
    # 删除前导和尾随的0
    bits = bits.strip('0')

    # 计算时间单位长度
    unit_length = min([len(match)
                      for match in bits.split('1') + bits.split('0')])

    # 构建正则表达式模式
    pattern = '1' * (3 * unit_length) + '0' * unit_length
    pattern += '|1' * unit_length + '0' * unit_length
    pattern += '|1' * (unit_length * 7) + '0' * unit_length
    pattern += '|0' * unit_length  # 用于匹配字符之间的空格

    # 通过正则表达式分割字符串
    parts = re.split(pattern, bits)

    morse_code = ''
    for part in parts:
        if part:
            morse_code += ' ' if len(part) > 3 * unit_length else ''
            morse_code += '.' if part[0] == '1' else '-'

    return morse_code


def decodeMorse(morseCode):
    words = morseCode.strip().split('   ')  # 用三个空格分割单词
    decoded_message = ''

    for word in words:
        characters = word.split()  # 用空格分割字符
        for character in characters:
            # 查找莫尔斯码对应的字母
            decoded_message += morse_code_dict.get(character, '')
        decoded_message += ' '  # 单词之间添加空格

    return decoded_message.strip()  # 去除前导和尾随空格


# 示例用法
bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"
morse_code = decodeBits(bits)
decoded_message = decodeMorse(morse_code)
print(decoded_message)
