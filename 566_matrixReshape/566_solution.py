class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        one_dim = []
        for row in nums:
            for col in row:
                one_dim.append(col)
        if (len(one_dim) != r * c):
            return nums
        else:
            result=[]
            for i in range(0,r):
                result.append(one_dim[i*c:(i*c)+c])
            return result