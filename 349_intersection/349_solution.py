class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection=[]
        for i in nums1:
            for j in nums2:
                if (i==j ):
                    if(i in intersection):
                        pass
                    else:
                        intersection.append(i)

        return intersection