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
    from DifficultyMedium.sol785IsBipartite import Solution
    graph = [[1,3], [0,2], [1,3], [0,2]]
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    ans = Solution().isBipartite(graph)
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