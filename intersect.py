class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        # 巧用python库中的Counter()来构造字典

        # 思路一： 只构造一个字典,nums2比较大时，节省一次构造的时间
        result = []   
        dic1 = Counter(nums1)
        for num in nums2:
            if num in dic1.keys():
                result.append(num)
                dic1[num] -= 1        # 通过字典操作实现检测个数的要求
                if dic1[num] == 0:
                    dic1.pop(num)            
        return result


          # 思路二： 构造两个字典则不用频繁的字典操作
#         result = []   
#         dic1,dic2 = Counter(nums1),Counter(nums2)

#         for num in dic2.keys():
#             if num in dic1.keys():
#                 repeat = min(dic1.get(num),dic2.get(num))
#                 for i in range(repeat):
#                     result.append(num)

#         return result
