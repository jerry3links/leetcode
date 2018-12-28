"""
    from DifficultyEasy.solE020ValidParent import Solution
    s = "()[]{}"
    print(s)
    ans = Solution().isValid(s)
    print(ans)
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l == 0:
            return True


        stack = []
        for i in range(l):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif s[i] == ")":
                if len(stack) <= 0:
                    return False
                top = stack.pop()
                if top == "(":
                    continue
                else:
                    return False
            elif s[i] == "]":
                if len(stack) <= 0:
                    return False
                top = stack.pop()
                if top == "[":
                    continue
                else:
                    return False
            elif s[i] == "}":
                if len(stack) <= 0:
                    return False
                top = stack.pop()
                if top == "{":
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False