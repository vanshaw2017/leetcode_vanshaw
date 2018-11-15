class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # 保证循环次数在0-len(nums)之间
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

# def rote_unit(nums):
#             temp = nums[-1]
#             for i in range(len(nums) - 1,0,-1):
#                 nums[i] = nums[i-1]
#             nums[0] = temp

#         if (k==0):
#             pass
#         else:
#             for i in range(0,k):
#                 rote_unit(nums)
