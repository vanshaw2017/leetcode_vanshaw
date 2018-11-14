class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result=[]
        cols=len(A[0])
        for i in range(0,cols):
            result.append([row[i] for row in A])
        return result