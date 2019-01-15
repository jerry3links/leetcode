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

    from BinaryTree.solM863DistanceKinBT import Solution
    root, target, K = Solution().constructCase()
    # root, target, K = Solution().constructCase2()
    Solution().printTree(root)
    ans = Solution().distanceK(root,target,K)
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