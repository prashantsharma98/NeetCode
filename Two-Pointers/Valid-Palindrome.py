# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

#----------------------------------------------------------------------------------------
# def palindrome(s):
#         l,r = 0,len(s)-1

#         while l<r:
#                 if s[l].lower() != s[r].lower():
#                         return False
#                 l+=1
#                 r-=1
#         return True
# Method1
#         t = []
#         for i in range(len(s)):
#             if self.isalphanum(s[i]):
#                 t.append(s[i].lower())
#         print(t)
#         print(list(reversed(t)))
#         return t == list(reversed(t))

# def isPalindrome(s):
#     l,r = 0, len(s)-1

#         while l < r:
#                 while l < r and not s[l].isalnum():
#                         l+=1

#                 while l < r and not s[r].isalnum():
#                         r-=1
#                 if s[l].lower() != s[r].lower():
#                         return False
#                 l+=1
#                 r-=1
                
#         return True


def isPalindrome(s):
    l,r = 0, len(s)-1
    while l < r:
        while l<r and not isalphanum(s[l]):
            l+=1
        while l<r and not isalphanum(s[r]):
            r-=1

        if s[l].lower() != s[r].lower():
            return False

        l+=1
        r-=1

    return True 

def isalphanum(c):
    return (
        ord("A") <= ord(c) <= ord("Z") 
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    )
if __name__ == "__main__":
    s = input()        
    print(isPalindrome(s))