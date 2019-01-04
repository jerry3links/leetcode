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


def stringToIntegerList(input):
    return json.loads(input)


def main():
    from DifficultyHard.solH065ValidNumber import Solution

    # s = "-90e3"
    # s = "+23e-123.132132123"

    # s = "23.123e132132123"
    # print(s)
    # ans = Solution().isNumber(s)
    # print("ans: {}".format(ans))
    #
    # # s = "23.e132132123"
    # s = "0.1"
    # print(s)
    # ans = Solution().isNumber(s)
    # print("ans: {}".format(ans))
    #
    # s = ".1"
    # print(s)
    # ans = Solution().isNumber(s)
    # print("ans: {}".format(ans))
    #
    # s = "   0123e12.12e123"
    # print(s)
    # ans = Solution().isNumber(s)
    # print("ans: {}".format(ans))

    # s = "2e0"
    s = ".0e"
    s = "46.e3"
    s = "32.e-80123"
    print(s)
    ans = Solution().isNumber(s)
    print("ans: {}".format(ans))

    # s = "53.5e93"
    # s = "  + "
    # s = "0.   "
    # s = "  ."
    # s = "  "

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