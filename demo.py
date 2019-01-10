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

    from DifficultyEasy.solE189RotateArray import Solution
    nums = [1,2,3,4,5,6,7]; k = 3
    # nums = [-1,-100,3,99]; k = 2
    nums = [1, 2]; k = 3
    print("nums: {}, k = {}".format(nums, k))
    Solution().rotate(nums, k)
    print("ans: {}".format(nums))




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