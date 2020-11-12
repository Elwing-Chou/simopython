# search(找到就好)/match(從頭開始)/findall
import re

pat = r"bbb"
target = "aaabbbccc"
result = re.search(pat, target)
print(result)

pat = r"b*"
target = "aaabbbccc"
result = re.search(pat, target)
print(result)

pat = r".+\t"
target = "aaabbb\tccc\t"
result = re.search(pat, target)
print(result)

pat = r".+?\t"
target = "aaabbb\tccc\t"
result = re.search(pat, target)
print(result)

# r, \. (), VERBOSE, group
pat = r"""
    ([a-z]+),          # name
    \s*                # blank
    (Mr|Mrs|Miss)\.    # 3 chose 1
    \s*                # blank
    ([a-z]+)           # surname
"""
target = "Elwing, Mr. Chou"
result = re.search(pat, target, re.VERBOSE | re.IGNORECASE)
print(result)
print(result.group(0))
print(result.groups())
