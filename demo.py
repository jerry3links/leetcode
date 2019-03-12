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
    from DP.solM063UniPathsII import Solution
    input = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    # input = [
    #     [1],
    #     [0]
    # ]
    print("input:\n{}".format(input))
    ans = Solution().uniquePathsWithObstacles(input)
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