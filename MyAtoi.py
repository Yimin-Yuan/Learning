class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        ret=re.findall(r"^[+-]?\d+",str.strip())
        if ret:
            ret_str=ret[0]
            ret_2=""
            if ret_str[0]=="+" or ret_str[0]=="-":
                ret_2=ret_str[1:]
            else:
                ret_2=ret_str
            ret_int=int(ret_2)
            if ret_str[0]=="-" and ret_int<2**31:
                return -ret_int
            elif ret_str[0]=="-" and ret_int>=2**31:
                return -2**31
            elif ret_int<=2**31-1:
                return ret_int
            elif ret_int>2**31-1:
                return 2**31-1
        else:
            return 0
                       
