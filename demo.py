import argparse
import json


def readlines():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The filename to be processed")
    args = parser.parse_args()
    if args.filename:
        with open(args.filename) as f:
            for line in f:
                yield line.strip('\n')


def stringToIntegerList(string):
    return json.loads(string)


def main():
    from Stack.solM150EvalRPN import Solution
    tokens = ["2", "1", "+", "3", "*"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]  # 22
    tokens = ["4", "13", "5", "/", "+"] # 6
    print(tokens)
    ans = Solution().evalRPN(tokens)

    print("ans = {}".format(ans))

if __name__ == '__main__':
    main()

# lines = readlines()
# while True:
#     try:
#         line = next(lines)
#         lst = stringToIntegerList(line)
#         print(lst)
#     except StopIteration:
#         break