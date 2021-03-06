# Leetcode 198. House Robber
# Easy 12/19/20 

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint 
# stopping you from robbing each of them is that adjacent houses have
# security system connected and it will automatically contact the police if
# two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without alerting the police.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Solution 1
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n<2:
            return nums[0]
        dp = [0] *n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]


    
# Time: O(a)
# Space: O(a)


# Solution 2

class Solution(object):
    def rob(self,nums):
        prev, cur = 0,0
        for value in nums:
            prev,cur = cur, max(prev+value, cur)
        return cur


# Time: O(a)
# Space: O(a)