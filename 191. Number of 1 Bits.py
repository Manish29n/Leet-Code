class Solution(object):
    def hammingWeight(self, n):
        b=[]
        while n!=0:
            if n%2==0:
                b.append(0)
            else:
                b.append(1)
            n//=2
        return b.count(1)
        """
        :type n: int
        :rtype: int
        """
