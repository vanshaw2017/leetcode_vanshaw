class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = []
        for i in ops:
            if i == '+':
                res.append(res[-1] + res[-2])
            elif i == 'C':
                res.pop()
            elif i == 'D':
                res.append(2 * res[-1])
            else:
                res.append(int(i))
        return sum(res)
