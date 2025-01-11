

import functools


class Solution:
    # def reverseBits(self, n: int) -> int:
    #     ret, power = 0, 24
    #     while n:
    #         temp2 = n & 0xFF
    #         temp3 = self.reverseByte(temp2) 
    #         temp = temp3 << power
    #         ret += temp
    #         temp4 = n >> 8
    #         n = temp4
    #         power -= 8
    #     return ret

    # # memoization with decorator
    # @functools.lru_cache(maxsize=256)
    # def reverseByte(self, byte):
    #     return (byte * 0x0202020202 & 0x010884422010) % 1023

    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            temp2 = (n & 1)
            temp = temp2 << power
            ret += temp
            n = n >> 1
            power -= 1
        return ret
    


if __name__ == '__main__':
    solution = Solution()

    print(solution.reverseBits(0b00000010100101000001111010011100))  # 964176192
    