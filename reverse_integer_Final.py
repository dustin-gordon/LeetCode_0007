class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        length = len(str(x))
        is_neg = False

        if(x < 0): 
			length -= 1
			is_neg = True
			x = abs(x)
        
        for i in range(length):
			result *= 10
			result += x % 10
			x //= 10

        if(is_neg):
			result *= -1
        if(result < -(2 ** 31)):
            result = 0
        if(result > (2 ** 31) - 1):
            result = 0
            
        return result