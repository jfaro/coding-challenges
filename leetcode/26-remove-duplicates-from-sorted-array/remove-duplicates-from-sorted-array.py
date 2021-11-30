class Solution:
    def removeDuplicates(self, nums) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


# Test cases
solution = Solution()

# 2, nums=[0,2,_]
nums = [1, 1, 2]
print(solution.removeDuplicates(nums))
print(nums)

# 5, nums=[0,1,2,3,4,_,_,_,_,_]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution.removeDuplicates(nums))
print(nums)
