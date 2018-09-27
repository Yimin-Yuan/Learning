class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        while m>0 and n>0:
            if nums1[m-1]<=nums2[n-1]:
                nums1[m+n-1]=nums2[n-1]
                n=n-1
            else:
                nums1[m+n-1]=nums1[m-1]
                m=m-1
        if n>0:
            nums1[:n]=nums2[:n]
        
        #nums1[m:m+n]=nums2[:n]
        #nums1.sort()