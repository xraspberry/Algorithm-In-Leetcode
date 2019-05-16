

available_positive_nums = [1, 3, 4]
available_negative_nums = [-1, -3, -4]


def sougou_interview(a, b):
    diff = abs(b - a)
    count = 0
    while diff > 0:
        if diff >= available_positive_nums[-1]:
            diff -= available_positive_nums[-1]
        elif diff >= available_positive_nums[-2]:
            diff -= available_positive_nums[-2]
        else:
            diff -= available_positive_nums[-3]
        count += 1
    return count


def sougou_dynamic(a, b):
    import sys
    nums = [1, 3, 4]
    dp = {
        1: 1,
        3: 1,
        4: 1
    }
    diff = abs(b-a)
    for i in range(2, diff+1):
        if i in dp:
            continue
        res = sys.maxsize
        for num in nums:
            if i - num > 0:
                res = min(res, dp[i-num])
        dp[i] = res + 1
    return dp[diff]


if __name__ == '__main__':
    res = sougou_dynamic(-1, -11)
    print(res)
    res = sougou_interview(1, 11)
    print(res)
