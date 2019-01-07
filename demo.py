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
    from DifficultyHard.solH065ValidNumber import Solution

    s_map = {
                "-90e3": True
                , "0": True
                , "+23e-123.132132123": False
                , "23.123e132132123": True
                , "23.e132132123": True,
                "0.1": True,
                ".1": True
                , "   0123e12.12e123": False
                , "2e0": True
                , ".0e": False
                , "46.e3": True
                , "32.e-80123": True
                , "53.5e93": True
                , "  + ": False
                , "0.   ": True
                , "   ": False
    }

    cnt = 0
    for k in s_map:
        try:
            assert Solution().isNumber(k) == s_map[k]
            # print("[{}]=>{}".format(k, Solution().isNumber(k)))
            cnt += 1
        except AssertionError:
            print("[{}] should be {}, cnt: {}".format(k, s_map[k], cnt))

    if cnt == len(s_map):
        print("All pass!")


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