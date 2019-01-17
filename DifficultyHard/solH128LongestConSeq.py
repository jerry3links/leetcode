"""
    from DifficultyHard.solH128LongestConSeq import Solution
    # nums = [100,4,200,1,3,2]
    # nums = [100, 4, 200, 199, 3, 198]
    # nums = [100, 4, 3, 101, 199]
    # nums = [2, 4, 3, 100, 7, 100, 103, 102,101]
    nums = [1,2,0,1] # 3
    nums = [-1, -9, -5, -2, -9, 8, -8, 1, -9, -3, -3] # 3
    print("nums: {}".format(nums))
    ans = Solution().longestConsecutive(nums)
    print("ans: {}".format(ans))
"""

class Solution(object):
    def longestConsecutive(self, nums):
        return self.secondImpl(nums)

    # 36ms~44ms (94.79%~53%)
    # using pair like (tail, counter) is slower (44ms)
    def secondImpl(self, nums):
        if len(nums) <= 1:
            return len(nums)

        nums.sort()

        tail = nums[0]
        counter = 1
        i = 1
        while i < len(nums):
            if nums[i] == tail + 1:
                tail = nums[i]
                counter += 1
                i += 1
            elif nums[i] == tail:
                i += 1
            else:
                if i + counter >= len(nums):
                    return counter
                else:
                    counter_tmp = 1
                    tail_tmp = nums[i]
                    j = i
                    while j < len(nums) and counter_tmp <= counter:
                        if nums[j] == tail_tmp + 1:
                            tail_tmp = nums[j]
                            counter_tmp += 1
                            j += 1
                        elif nums[j] == tail_tmp:
                            j += 1
                        else:
                            break
                    if counter_tmp > counter:
                        counter = counter_tmp
                        tail = tail_tmp
                    i = j

        return counter


    # 52ms
    def firstImpl(self, nums):
        if len(nums) <= 1:
            return len(nums)

        nums.sort()

        basket = [nums[0]]
        i = 1
        while i < len(nums):
            if nums[i] == basket[-1] + 1:
                basket.append(nums[i])
                i += 1
            elif nums[i] == basket[-1]:
                i += 1
            else:
                if i + len(basket) >= len(nums):
                    return len(basket)
                else:
                    tmp = [nums[i]]
                    j = i
                    while j < len(nums) and len(tmp) <= len(basket):
                        if nums[j] == tmp[-1] + 1:
                            tmp.append(nums[j])
                            j += 1
                        elif nums[j] == tmp[-1]:
                            j += 1
                        else:
                            break
                    if len(tmp) > len(basket):
                        basket = tmp
                    i = j

        return len(basket)