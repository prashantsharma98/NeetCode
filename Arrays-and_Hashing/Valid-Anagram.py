# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

#-----------------------------------------------------------------------------------------------------
def isAnagram(s,t):
    #Solution 1
    # s= list(s)
    # t = list(t)
    # return sorted(s) == sorted(t)

    #Solution 2
    #If length of the two strings are different, return False
    # if len(s) != len(t):
    #     return False
    # #Set for all the letters in the string 's'
    # remove_duplicate = set(s)
    # for c in remove_duplicate:
    #     #If the number of the letters in 's' is different from 't', return False
    #     if s.count(c) != t.count(c):
    #         return False

    # return True
    # Solution 3
    if len(s) != len(t):
        return False
    dict1, dict2 = {}, {}
    for i in range(len(s)):
        dict1[s[i]] = 1 + dict1.get(s[i], 0)
        dict2[t[i]] = 1 + dict2.get(t[i], 0)

    return dict1 == dict2 


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s,t))
 
    