import math


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(M)
        cols = len(M[0])
        result = []

        for i in range(0, rows):
            new_row = []
            for j in range(0, cols):
                sum1 = 0
                list1 = [i - 1, i, i + 1]
                list2 = [j - 1, j, j + 1]
                a = [elem for elem in list1 if ((elem >= 0) and (elem < rows))]
                b = [elem for elem in list2 if ((elem >= 0) and (elem < cols))]
                count = len(a) * len(b)
                for m in a:
                    for n in b:
                        sum1 += M[m][n]
                new_row.append(math.floor(sum1 / count))
            result.append(new_row)
        return result
