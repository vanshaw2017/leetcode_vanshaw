class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        lenth=len(A)
        for i in A:
            if (A.count(i)==lenth/2):
                return i
                break