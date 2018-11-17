class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #先写一个字典保存零的位置
        zero_list=[]
        for i in range(0,len(nums)):
            if(nums[i]==0):
                zero_list.append(i)
        count=0
        for i in zero_list:
            nums.remove(nums[i-count])
            count+=1
        for i in range(0,count):
            nums.append(0)