from collections import Counter

# def longestPalindrome(s: str) -> int:

#         d = Counter(s).values()
#         print(d)
#         return sum(2 * (c // 2) for c in d) + any(c % 2 == 1 for c in d)




# s = "aabbcccdddh"

# print(longestPalindrome(s))

# print(Counter(s).values())

###any is true if there exist a single true value in list even if all others all false
# print(any(i for i in s))


##2 easy to read way
def longestPalindrome(s: str) -> int:

        char_count = {}
        final_count = 0
        odd_exist = False
        for i in s:
                char_count[i] = char_count.get(i,0) + 1
        for char in char_count:
                if char_count[char] % 2 == 0:
                        final_count += char_count[char]
                else:
                        final_count += (char_count[char] - 1)
                        odd_exist = True
        if odd_exist:
                final_count += 1

        return final_count

s = "aabbcccdddh"

print(longestPalindrome(s))
