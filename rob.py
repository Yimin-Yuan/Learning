class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        if len(nums)==1:
            return max(nums)
        
        length=len(nums) 
        money=[0]*length
        money[0]=nums[0]
        money[1]=max(nums[1],nums[0])
        for i in range(2,length):  
            #是否打劫nums[i]? 比较money[i-2]+nums[i]与money[i-1]  
            money[i]=max(money[i-2]+nums[i],money[i-1])  
        return money[length-1] 
