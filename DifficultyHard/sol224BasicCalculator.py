
"""
    from Difficulty.sol224BasicCalculator import Solution
    strs = "(1+(4+5+2)-3)+(6+8)"
    print("que: {}".format(strs))
    a = Solution().calculate(strs)
    print("ans: {}".format(a))

    strs = " ( 3)"
    print("que: {}".format(strs))
    a = Solution().calculate(strs)
    print("ans: {}".format(a))

    strs = " 2-1 + 2 "
    print("que: {}".format(strs))
    a = Solution().calculate(strs)
    print("ans: {}".format(a))

    strs = "(1-(13-104))"
    print("que: {}".format(strs))
    a = Solution().calculate(strs)
    print("ans: {}".format(a))
"""



class Solution:


    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = []

        s = s.replace(" ", "")

        for c in s:
            if c == ")":
                curr = stack.pop()
                prev = None
                num = 0
                while curr != "(":
                    if curr == "+":
                        num += int(prev)
                    elif curr == "-":
                        num -= int(prev)
                    prev = curr
                    curr = stack.pop()
                num += int(prev)
                stack.append(str(num))

            elif c.isdigit():
                if stack:
                    tail = stack[-1]
                    if tail[-1].isdigit():
                        tmp = stack.pop()
                        tmp = tmp + c
                        stack.append(tmp)
                    else:
                        stack.append(c)
                else:
                    stack.append(c)
            else:
                stack.append(c)

        curr = stack.pop()
        prev = 0
        res = 0
        while stack:
            if curr == "+":
                res += int(prev)
            elif curr == "-":
                res -= int(prev)
            prev = curr
            curr = stack.pop()
        res += int(curr)

        return res