"""
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
"""


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        return self.firstImpl(IP)

    def firstImpl(self, IP):
        char_list = list(IP)
        isV4 = True if '.' in char_list else False
        isV6 = True if ':' in char_list else False

        if isV4:
            elements = IP.split(".")
            if len(elements) != 4:
                return "Neither"
            for v in elements:
                if len(v) > 1:
                    digits = list(v)
                    while digits:
                        c = digits.pop(0)
                        if not c.isdigit():
                            return "Neither"
                        if c == '0':
                            return "Neither"
                elif len(v) <= 1:
                    if not v.isdigit():
                        return "Neither"
                else:
                    return "Neither"
                if int(v) < 0 or int(v) > 255:
                    return "Neither"
            return "IPv4"
        elif isV6:
            elements = IP.split(":")
            if len(elements) != 8:
                return "Neither"
            for v in elements:
                if len(v) > 4:
                    return "Neither"
                elif len(v) == 0:
                    return "Neither"
                digits = list(v)
                while digits:
                    c = digits.pop(0)
                    if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                 'a', 'b', 'c', 'd', 'e', 'f',
                                 'A', 'B', 'C', 'D', 'E', 'F']:
                        return "Neither"
                if int(v, 16) < 0 or int(v, 16) > 65535:
                    return "Neither"
            return "IPv6"

        return "Neither"