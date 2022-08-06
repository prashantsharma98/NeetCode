def groupAnagrams(strs):
    dict1, arr = {}, []
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in dict:
            dict[sorted_word]
