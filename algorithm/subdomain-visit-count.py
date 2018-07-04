class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        counter = defaultdict(int)
        for cpdomain in cpdomains:
            times, domain = cpdomain.split(' ')
            elements = domain.split('.')
            idx = 0
            while idx < len(elements):
                subdomain = '.'.join(elements[idx:])
                counter[subdomain] += int(times)
                idx += 1
        return ["{} {}".format(value, key) for key, value in counter.items()]


if __name__ == '__main__':
    print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
