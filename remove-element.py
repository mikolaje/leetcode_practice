#coding=utf-8
class Solution:
    def removeElement(self,A,elem):
        i,last=0,len(A)-1
        while i<=last:
            if A[i]==elem:
                A[i],A[last]=A[last],A[i]
                last-=1
            else:
                i+=1

        return last+1

if __name__=='__main__':
    print(Solution().removeElement([1,2,3,4,5,2,3],2))