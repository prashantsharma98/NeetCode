# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

#---------------------------------------------------------------------------------------------------------------


def containsDuplicate(nums):
    #Initiallizing a set for storing all the numbers
    hashset = set()
    for n in nums:
        if n in hashset:
            #If the set contains the number already, return True
            return True
        #If the set doesn't contains the number already, add the number for next time
        hashset.add(n)
    #Return False if no number if repeated
    return False


if __name__ == "__main__":
    nums = [1,2,3,4]
    print(containsDuplicate(nums))