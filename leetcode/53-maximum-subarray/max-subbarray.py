# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5, 4, -1, 7, 8]
# Output: 23

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = []
        max_subarray_sum = float('-inf')

        # Init array
        for i in range(0, len(nums)):
            row = []
            for j in range(0, len(nums)):
                row.append('X')
            dp.append(row)

        # DP
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):

                # Base case (subarray of length 1)
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j - 1] + nums[j]

                if dp[i][j] > max_subarray_sum:
                    max_subarray_sum = dp[i][j]

        return max_subarray_sum


solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))    # 6
print(solution.maxSubArray([1]))                                # 1
print(solution.maxSubArray([5, 4, -1, 7, 8]))                   # 23
print(solution.maxSubArray([-57, 9, -72, -72, -62, 45, -97, 24, -39, 35, -
                            82, -4, -63, 1, -93, 42, 44, 1, -75, -25, -87, -16, 9, -59, 20, 5, -95]))
