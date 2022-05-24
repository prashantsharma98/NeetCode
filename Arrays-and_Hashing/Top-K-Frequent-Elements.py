# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# -------------------------------------------------------------------------------------------------------------------


def topKFrequent(nums, k):
    # Create a dict for storing the numbers and freq
    dict1 = {}
    # Iterate over 'nums'
    for i in range(len(nums)):
        if nums[i] in dict1.keys():
            dict1[nums[i]] += 1

        else:
            dict1[nums[i]] = 1
    
    arr = sorted(dict1.items(), key = lambda kv:(kv[1], kv[0]))
    for j in range(k):
        
    # print(dict1)
    # arr = []
    # for j in dict1.keys():
        
    #     if dict1[j] == k:
    #         arr.append(j)
    # return arr

if __name__ == "__main__":
    
    
    nums = [2,2,1,2,1,3] 
    k = 2
    print(topKFrequent(nums,k))

