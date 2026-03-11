# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

# 1. Read the input and immediately make it all uppercase
word = input().upper()

# 2. Extract only the unique letters using set(), and turn it back into a list
unique_letters = list(set(word))

# 3. Create an empty list to store our counts
counts = []

# Loop through each unique letter and count it in the original word
for letter in unique_letters:
    # word.count(letter) counts how many times the letter appears!
    cnt = word.count(letter)
    counts.append(cnt)

# 4. Find the highest count (the max score)
max_count = max(counts)

# 5. The Tie-Breaker Logic
# If the max score appears more than once in our counts list, it's a tie!
if counts.count(max_count) > 1:
    print("?")
else:
    # Otherwise, find the exact position (index) of the winning score
    max_index = counts.index(max_count)
    # Print the letter that matches that winning position!
    print(unique_letters[max_index])
