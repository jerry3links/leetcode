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

    from DifficultyEasy.solE021MergeSortedLists import Solution
    l1, l2 = Solution().constructCase()
    print("l1:")
    Solution().printList(l1)
    print("l2:")
    Solution().printList(l2)
    ans = Solution().mergeTwoLists(l1, l2)
    print("ans:")
    Solution().printList(ans)

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