class Solution:
    def isHappy(self, n: int) -> bool:

        #make the int a string so that we can split

        #memoize it, if we've already seen it we're doomed


        mem = set()
        
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])

            if n in mem:
                return False
            else:
                mem.add(n)

        return True
