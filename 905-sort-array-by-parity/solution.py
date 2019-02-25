class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        def is_even(num):  # 偶数
            if (num % 2 != 0):
                return False
            else:
                return True

        even_list = []
        odd_list = []
        for i in A:
            if is_even(i):
                even_list.append(i)
            else:
                odd_list.append(i)
        return even_list + odd_list
