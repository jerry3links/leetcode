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
    from BitManipulation.solM137SingleNumII import Solution
    nums = [2,2,3,2]
    nums = [0,1,0,1,0,1,99]
    nums = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
    print("nums: {}".format(nums))
    ans = Solution().singleNumber(nums)
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