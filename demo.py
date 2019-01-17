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

    from DifficultyHard.solH128LongestConSeq import Solution
    # nums = [100,4,200,1,3,2]
    # nums = [100, 4, 200, 199, 3, 198]
    # nums = [100, 4, 3, 101, 199]
    # nums = [2, 4, 3, 100, 7, 100, 103, 102,101]
    nums = [1,2,0,1] # 3
    nums = [-1, -9, -5, -2, -9, 8, -8, 1, -9, -3, -3] # 3
    print("nums: {}".format(nums))
    ans = Solution().longestConsecutive(nums)
    print("ans: {}".format(ans))

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