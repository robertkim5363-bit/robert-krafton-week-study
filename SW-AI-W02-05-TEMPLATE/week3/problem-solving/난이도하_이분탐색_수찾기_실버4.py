# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
import sys

# 1. Reading input this way is much faster for large data (100,000 lines)
input = sys.stdin.read().split()

# 2. Assign the values based on their position in the input list
n = int(input[0])
# We store the target numbers in a SET for O(1) search speed
n1 = set(input[1:n+1])

m = int(input[n+1])
m1 = input[n+2:]

# 3. Check each number in M against our Set N
for x in m1:
    if x in n1:
        print(1)
    else:
        print(0)
