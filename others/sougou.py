

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


if __name__ == '__main__':
    res = sougou_interview(1, 6)
    print(res)
