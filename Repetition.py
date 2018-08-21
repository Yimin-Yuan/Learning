class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==[]:
            return False
        else:
            dic=collections.Counter(nums)
            for value in dic.values():
                if value>=2:
                    return True
            return False