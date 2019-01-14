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

    from DifficultyMedium.solM468ValidIP import Solution
    benches = {
        "172.16.0.1": "IPv4",
        "172.16.254.00001": "Neither",
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334": "IPv6",
        "2001:db8:85a3:0:0:8A2E:0370:7334": "IPv6",
        "2001:0db8:85a3::8A2E:0370:7334": "Neither",
        "02001:0db8:85a3:0000:0000:8a2e:0370:7334": "Neither",
        "1e1.4.5.6": "Neither",
        "1.0.1.": "Neither"
    }
    cnt = 0
    for IP in benches:
        try:
            assert Solution().validIPAddress(IP) == benches[IP]
            cnt += 1
        except AssertionError:
            print("[{}] should be {}, cnt: {}".format(IP, benches[IP], cnt))

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