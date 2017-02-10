#coding=utf-8

class Solution:
    def plusOne(self,digits):
        carry=1
        print (range(len(digits)))
        for i in reversed(range(len(digits))):
            digits[i]+=carry #这一步是为了计算出新的carry
            carry=digits/10
            digits[i]%=10
        if carry:
            digits=[1]+digits


        return digits

    def plusOne2(self,digits):
        digits=[str(x) for x in digits]
        num=int(''.join(digits))+1
        return [int(x) for x in str(num)]

if __name__=='__main__':
    print Solution().plusOne([9,9,9,9])