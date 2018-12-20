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
    from DifficultyMedium.sol279PerfectSquareDP import Solution
    n_lst = [0, 1, 12, 13]
    for n in n_lst:
        print("n: {}".format(n))
        a = Solution().numSquares(n)
        print("num of ps: {}".format(a))


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