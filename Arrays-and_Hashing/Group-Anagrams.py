# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

#------------------------------------------------------------------------------------------------------

# # Solution 1:
# def groupAnagrams(strs):
    
#     # Initialize the dictionary to store the values for every anagram and the final array
#     dict, arr = {}, []
#     # Iterate for every word in the 'strs'.
#     for word in strs:
#         # Sort the word for comparing the anagram
#         sorted_word = "".join(sorted(word))
#         # If anagram in dictionary, just add the word
#         if sorted_word in dict:
#             dict[sorted_word].append(word)
#         # If anagram not in the dict, add a new anagram
#         else:
#             dict[sorted_word] = [word]


#     # print(dict)
#     for a in dict:
#         # Append all the words for a particular anagram in the dictionary to the final array
#         arr.append(dict[a])

#     return(arr)

# Solution 2
from collections import defaultdict


def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c)- ord('a')] += 1
        res[tuple(count)].append(s)
    return res.values()
    

if __name__ == "__main__":
    
    
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))
        