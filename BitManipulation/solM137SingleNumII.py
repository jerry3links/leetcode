"""
    from BitManipulation.solM137SingleNumII import Solution
    nums = [2,2,3,2]
    nums = [0,1,0,1,0,1,99]
    nums = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
    print("nums: {}".format(nums))
    ans = Solution().singleNumber(nums)
    print("ans = {}".format(ans))
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res= 0
        cnt = [0 for _ in range(33)]

        for n in nums:
            if n < 0:
                cnt[-1] += 1

        for i in range(32):
            for n in nums:
                if n < 0:
                    n = -n
                cnt[i] += (n >> i) & 1
            res |= (cnt[i] % 3) << i

        if cnt[-1] % 3 == 1:
            res = -res

        return res

    def thirdImpl(self, nums):

        def num2bin(num):
            i = 0
            if num < 0:
                num = -num
                count[32] += 1 # apply signed bit
            while num > 0:
                num, r = divmod(num, 2) # shift right
                count[i] += r
                i += 1

        def bin2num(binary):
            mult = 1
            ans = 0
            for i in range(len(binary) - 1):
                ans += mult * binary[i]
                mult *= 2 # shift left
            return ans

        count = [0] * 33

        for n in nums:
            num2bin(n)

        s = [str(b) for b in count]
        print("count: {}".format("".join(s)))

        for i in range(len(count)):
            count[i] %= 3
        s = [str(b) for b in count]
        print("count (mod 3): {}".format("".join(s)))
        res = bin2num(count)
        print("res: {}".format(res))
        return res if count[-1] == 0 else -res

    def secondImpl(self, nums):
        d = {}

        for val in nums:
            if val in d:
                d[val] += 1
            else:
                d[val] = 1

        for k in d:
            if d[k] == 1:
                return k


    def firstImpl(self, nums):

        result = 0
        count = [0 for _ in range(33)]
        for i in range(32):
            for j in range(len(nums)):
                if (nums[j] >> i) & 1 == 1:
                    count[i] += 1
            result |= count[i] % 3 << i
            # print("{} ({}) ...".format(result, bin(result)))
        return result