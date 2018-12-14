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
    from DifficultyMedium.sol300LIS import Solution
    nums = [10,9,2,5,3,7,101,18]
    nums = [10, 9, 2, 5, 3, 4]
    # nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print("nums: {}".format(nums))
    ans = Solution().lengthOfLIS(nums)
    print(ans)


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