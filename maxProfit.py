class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        profile=0
        Min=prices[0]
        for p in prices:
            profile=max(profile,p-Min)
            Min=min(Min,p)
        return profile
            
