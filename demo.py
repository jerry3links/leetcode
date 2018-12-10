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
    from DifficultyHard.sol224BasicCalculator import Solution
    strs = "(1+(4+5+2)-3)+(6+8)"
    print("que: {}".format(strs))
    a = Solution().calculate(strs)
    print("ans: {}".format(a))


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