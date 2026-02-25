"
Partition Equal Subset Sum


Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
----------------------------------------------------------------"

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:  return False

        target = total // 2
        n = len(nums)

        dp = [[-1] * (target + 1) for _ in range(n)]

        return self.rec(nums, target, 0, dp)

    def rec(self, nums, target, i, dp):
        if target == 0:
            return True
        if i >= len(nums)  :
            return False
        if dp[i][target] != -1:
            return dp[i][target]

        pick = self.rec(nums, target - nums[i], i + 1, dp)
        not_pick = self.rec(nums, target, i + 1, dp)
        dp[i][target] = pick or not_pick
        
        return dp[i][target]