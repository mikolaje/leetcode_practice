class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        index = 0
        while (len(bits) - index) >= 0:
            if len(bits) - index == 1:
                return True
            if len(bits) - index == 0:
                return False
            if bits[index] == 1:

                index += 2
            else:

                index += 1

