class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for each_row in A:
            i = 0
            j = len(each_row) - 1
            while (i <= j):
                temp = each_row[j]
                each_row[j] = 1 - each_row[i]
                each_row[i] = 1 - temp
                i += 1
                j -= 1
        return A

