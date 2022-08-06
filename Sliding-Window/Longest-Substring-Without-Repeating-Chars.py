# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

#------------------------------------------------------------------------------------------------------




def LongestSubstring(s):
    #Seen dict for storing all the repeating chars and their indexes
    seen = {}
    # l is the left index value for our window for the length of the substr
    l = 0
    # output is for storing the longest substr length
    output = 0
    for i in range(len(s)):
        #Iterating over all the chars, checking if the char is unique, just increasing the output value by one
        if s[i] not in seen:
            output = max(output, i-l+1)
        #If a char is repeating, then we check if s[i] is in the substr or not
        else:
            # The char's last index for the repeating value is left of the l index, so just increase the output value by one, because it does not effect the substr
            if seen[s[i]] < l:
                output = max(output, i-l+1)
            # The char's last index for the repeating value is right of the l index, so it effects the substr, so we remove all the chars before the last index of the s[i] value 
            else:
                l = seen[s[i]] + 1  
        # Adding the char in the dict with the last index of the char 
        seen[s[i]] = i

    return output

if __name__ == "__main__":
    s = 'bbbbbb'
    print(LongestSubstring(s))
