# 返回给定字符串中元音的数量（计数）。对于这个Kata，我们将考虑a、e、i、o、u作为元音（但不包括y）。输入的字符串将只由小写字母和/或空格组成。

def get_count(sentence):
  count = 0
  vowels = ['a', 'e', 'i', 'o', 'u']
  for letter in sentence:
    if letter in vowels:
      count += 1
  return count

print(get_count("Hello aaaaa"))