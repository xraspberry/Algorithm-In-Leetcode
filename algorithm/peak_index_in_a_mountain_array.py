class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return
        lo = 0
        hi = len(A) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                return mid
            elif A[mid] >= A[mid - 1]:
                lo = mid + 1
            elif A[mid] >= A[mid + 1]:
                hi = mid - 1


if __name__ == '__main__':
    A = [0, 1, 0]
    print(Solution().peakIndexInMountainArray(A))
