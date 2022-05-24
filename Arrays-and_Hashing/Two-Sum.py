# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

#------------------------------------------------------------------------------------------




def twoSum(nums, target):
    # Solution 1: O(n*2)
    # Iterating over the arr twice, getting all the pairs for comparison
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         #If sum equals to target, return the array of indices
    #         if nums[i]+nums[j] == target:
    #             return [i,j]
    # Solution 2: O(n)
    # Create a dict for storing the diff of the number 
    difflist = {}

    for i in range(len(nums)):
        # Diff of the number from the target 
        diff = target - nums[i]
        # If the diff of the target and the current number is in the dict, than we get the pair which is adding up to the target
        if diff in difflist:
            return [difflist[diff],i]
        # Adding the difference for future comaparison 
        difflist[nums[i]] = i

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    print(twoSum(nums, target))