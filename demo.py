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
    from DifficultyMedium.solM012Int2Roman import Solution

    benches = {
                3: "III"
                , 4: "IV"
                , 9: "IX"
                , 10: "X"
                , 58: "LVIII" ,
                1994: "MCMXCIV"
    }

    cnt = 0
    for val in benches:
        try:
            assert Solution().intToRoman(val) == benches[val]
            cnt += 1
        except AssertionError:
            print("[{}] should be [{}], cnt: {}".format(val, benches[val], cnt))

    if cnt == len(benches):
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