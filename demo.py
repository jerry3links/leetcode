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
    from DifficultyMedium.sol322CoinChange import Solution
    # coins = [1,2,5]; amount =11
    coins = [474, 83, 404, 3]; amount = 264
    # coins =[125, 146, 125, 252, 226, 25, 24, 308, 50]
    # amount = 8402
    # coins = [94, 91, 377, 368, 207, 40, 415, 61]
    # amount = 9662
    print("coins = {}; amount = {}".format(coins, amount))
    ans = Solution().coinChange(coins, amount)

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