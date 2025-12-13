from collections import Counter
def first_freq(s):
    count=Counter(s)
    #seen=set()
    for char in s:
        if count[char]==1:
            return char
    return None
s="swiss"
print(first_freq(s))