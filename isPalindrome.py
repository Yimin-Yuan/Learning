class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s2=re.sub("[^a-z0-9]","",s.lower())
        if s2==[]:
            return True
        if s2==s2[::-1]:
            return True
        else:
            return False
