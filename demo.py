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
    from DifficultyEasy.sol155MinStack import MinStack
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    a = obj.getMin()
    print("getMin(): {}".format(a))
    obj.pop()
    print("pop ...")
    a = obj.top()
    print("top: {}".format(a))
    a = obj.getMin()
    print("getMin(): {}".format(a))


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