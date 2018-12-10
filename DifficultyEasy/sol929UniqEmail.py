"""
    from DifficultyEasy.sol929UniqEmail import Solution
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"]
    ans = Solution().numUniqueEmails(emails)
    print(ans)
"""


class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emailSet = set()
        for email in emails:
            strList = list(email)
            if "@" not in strList:
                continue
            domainName = email[strList.index("@"):]

            localNameWithDot = ""
            if "+" in strList:
                localNameWithDot = email[:strList.index("+")]
            localName = localNameWithDot.replace(".", "")
            uniqEmail = localName + domainName
            emailSet.add(uniqEmail)


        cnt = len(emailSet)



        return cnt
