def find_password(words):
  word_set = set(words)
  for word in words:
    reversed_word = word[::-1]
    if reversed_word in word_set:
      length = len(word)
      mid_index = length // 2
      return length, word[mid_index]
