"""
    from Stack.solM150EvalRPN import Solution
    tokens = ["2", "1", "+", "3", "*"] # 9
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"] # 22
    # tokens = ["4", "13", "5", "/", "+"] # 6
    print(tokens)
    ans = Solution().evalRPN(tokens)
    print("ans = {}".format(ans))
"""


class Solution(object):

    operators = ['+', '-', '*', '/']

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        oprd_stk = []
        while tokens:

            t = tokens.pop(0)

            if t in self.operators:
                b = float(oprd_stk.pop())
                a = float(oprd_stk.pop())
                c = ""
                if t == '+':
                    c = str(int(a + b))
                elif t == '-':
                    c = str(int(a - b))
                elif t == '*':
                    c = str(int(a * b))
                elif t == '/':
                    X = a / b
                    print("a / b = {}".format(X))
                    Y = (round(a / b, 1)) # round to 1 digit after the decimal point
                    print("round: {}".format(Y))
                    c = str(int(Y))
                oprd_stk.append(c)
                # print("{} OP {} = {}".format(a,b,c))
            else:
                oprd_stk.append(t)

        # print(oprd_stk)

        return int(oprd_stk[0])

