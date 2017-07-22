'''

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 ? i ? N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

这道题一开始的思路就是暴力解决，生成所有的可能，然后取判断，当然在N小的时候可以在规定的时间算出来，但是多了之后就time limit exceeded

'''


class SolutionA(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def judge(num, pos):
            if not (num % pos) or not (pos % num):
                return True
            return False

        from itertools import permutations
        seq = range(1, N + 1)
        seq_len = len(seq)
        count = 0
        for arrangement in (permutations(seq, seq_len)):
            for index, ele in enumerate(arrangement, 1):
                res = judge(ele, index)
                if not res:
                    break
            else:
                count += 1

        return count


class SolutionB(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        # 另外一种思路，就是动态规划
        # 对于2个元素的时候，有两种可能，1，2和2，1，这个结果是如何出来的呢
        # 首先动态规划就是该问题由重叠子问题，这样可以用空间换时间
        # 另外最优子结构，就是大问题可以由小问题解决
        # 这道题要求出N=2时候的解，可以参考N=1时候的解，但是必须要保证在第二个位置确定好可以被整除的元素后，再去寻找N=1时候的解
        # 那么对于N=3时候，就是先确定可以被三整除的元素，将其确定后，再在剩余2个元素寻找N=2时候的解
        # 有思路后，就开始编码吧

        # 非缓存版本，accepted，实现了大致的思路，但是动态规划正是因为缓存，使用空间换时间，已经计算过的不再计算才是动态规划的优势
        # Runtime: 165 ms Your runtime beats 84.64 % of python submissions.
        def find_arrangement(i, arrange):
            if i == 1:
                return 1
            total = 0
            for index, ele in enumerate(arrange):
                if ele % i == 0 or i % ele == 0:
                    total += find_arrangement(i - 1, arrange[:index] + arrange[index + 1:])
            return total

        from functools import wraps

        def memo(func):
            cache = {}

            @wraps(func)
            def inner(*args):
                if args in cache:
                    return cache[args]
                res = func(*args)
                cache[args] = res
                return res

            return inner

        # 缓存版本，效率明显提升！Runtime: 82 ms Your runtime beats 90.89 % of python submissions.
        @memo
        def find_arrangement_cache(i, arrange):
            if i == 1:
                return 1
            total = 0
            for index, ele in enumerate(arrange):
                if ele % i == 0 or i % ele == 0:
                    total += find_arrangement_cache(i - 1, arrange[:index] + arrange[index + 1:])
            return total

        return find_arrangement_cache(N, tuple(range(1, N + 1)))


if __name__ == "__main__":
    res = SolutionB().countArrangement(10)
    print(res)