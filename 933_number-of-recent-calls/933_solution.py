
#这个问题非常简单，最简单的思路就是使用队列，
# 队列中维护当前时间[t-3000,t]这个区间的全部元素，
# 最后返回的结果就是这个队列的长度。

class RecentCounter:
    def __init__(self):
        self.pings = list()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        while self.pings[0] < t - 3000:
            self.pings.pop(0)
        return len(self.pings)
