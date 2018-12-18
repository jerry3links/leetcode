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
    from DifficultyMedium.sol518CoinChangeII import Solution
    # amount = 5; coins = [1,2,5, 10]
    amount = 5; coins = [1, 2, 5]
    # amount = 10; coins = [10]
    # amount = 3; coins = [2]
    print("amount: {}, coins: {}".format(amount, coins))

    ans = Solution().change(amount, coins)
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