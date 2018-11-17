class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        result = []
        for i in nums:
            if (i not in dict1):
                dict1.update({i: 1})
            else:
                dict1[i] += 1

        max_index = max(dict1.values())
        for key, value in dict1.iteritems():
            if value == max_index:
                return key
