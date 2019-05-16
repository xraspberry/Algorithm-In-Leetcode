class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = ''.join(S.split('-')).upper()
        # 从后面往前遍历，每到一组就将结果放入结果集
        i = len(S) - 1
        j = len(S)
        count = 1
        res = []
        while i >= 0:
            if count % K == 0:
                res.append(S[i:j])
                j = i
                count = 1
            else:
                count += 1
            if i == 0 and S[i:j]:
                res.append(S[i:j])
            i -= 1
        return '-'.join(res[::-1])


if __name__ == '__main__':

    S = "2-5g-3-J"
    K = 2
    res = Solution().licenseKeyFormatting(S, K)
    print(res)
    assert res == "2-5G-3J"

    S = "5F3Z-2e-9-w"
    K = 4
    res = Solution().licenseKeyFormatting(S, K)
    print(res)
    assert res == "5F3Z-2E9W"
