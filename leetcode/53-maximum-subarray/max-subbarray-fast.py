class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        global_max_sum = nums[0]
        current_max_sum = nums[0]

        for i in range(1, len(nums)):
            current_max_sum = max(current_max_sum + nums[i], nums[i])
            global_max_sum = max(global_max_sum, current_max_sum)

        return global_max_sum


solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))    # 6
print(solution.maxSubArray([1]))                                # 1
print(solution.maxSubArray([5, 4, -1, 7, 8]))                   # 23
