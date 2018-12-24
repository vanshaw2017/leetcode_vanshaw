class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag1=[]#zeng
        flag2=[]#减
        for i in range(0,len(A)-1):
            if (A[i]<=A[i+1]):
                flag1.append(1)
            if(A[i]>=A[i+1]):
                flag2.append(0)
        if (flag1.count(1)==len(A)-1 or flag2.count(0)==len(A)-1):
            return True
        else:
            return False