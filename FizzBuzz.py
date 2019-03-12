class Solution:
    def fizzBuzz(self, n: int):
        List=[]
        if n==0 :
            return List
        for i in range(n):
            if ((i+1) % 3==0) and ((i+1) % 5 ==0):
                List.append('FizzBuzz')
            elif ((i+1) % 3 == 0):
                List.append('Fizz')
            elif ((i+1) % 5 == 0):
                List.append('Buzz')
            else:
                List.append(str(i+1))        
        return List
