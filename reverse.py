class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10<x<10:
            return x
        a=str(abs(x))
        for i in range(len(a)):
            b=a[::-1]
        if x<0:
            result=-int(b)
        else:
            result=int(b)
        if -2147483648 < result < 2147483647:
            return result
        else:
            return 0
        
