class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:]=zip(*matrix[::-1])
        #zip函数：zip() 函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象。如果各个可迭代对象的元素个数不一致，则返回的对象长度与最短的可迭代对象相同。利用 * 号操作符，与zip相反，进行解压。
        #a[::-1]:相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍
       
       
