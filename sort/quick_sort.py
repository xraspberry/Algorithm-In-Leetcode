class Solution:
    def partition(self, nums):
        pi, nums = nums[0], nums[1:]
        lo = [x for x in nums if x <= pi]
        hi = [x for x in nums if x > pi]
        return pi, lo, hi

    def quick_sort(self, nums):
        if not nums:
            return []
        pi, lo, hi = self.partition(nums)
        return self.quick_sort(lo) + [pi] + self.quick_sort(hi)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quick_sort(nums)[-k]


def quick_sort1(array, l, r):
    if l < r:
        q = partition1(array, l, r)
        quick_sort1(array, l, q - 1)
        quick_sort1(array, q + 1, r)
    return array


def partition1(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        # i记录的是上次比较大的元素
        # 所以出现小元素之后，就会将小元素和大元素交换位置
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    # i+1就是当前切分元素，也就是i+1之前都是比x小的
    # i+1之后就是比x大的
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quick_sort(nums, low, high):
    if low < high:
        key_index = partition(nums, low, high)
        quick_sort(nums, low, key_index)
        quick_sort(nums, key_index + 1, high)
    return nums


def partition(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]
        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort_iter(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])


def merge_sort(nums):
    """
    归并排序
    :param nums:
    :return:
    """
    # 切分数组
    mid = len(nums) // 2
    lft, rgt = nums[:mid], nums[mid:]
    if len(lft) > 1:
        lft = merge_sort(lft)
    if len(rgt) > 1:
        rgt = merge_sort(rgt)
    res = []
    # 归并的时候lft和rgt已经有序
    while lft and rgt:
        # 先由大到小append
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


# 选择第k大的元素
def select(nums, k):
    pi, nums = nums[0], nums[1:]
    lo = [num for num in nums if num <= pi]
    hi = [num for num in nums if num > pi]
    m = len(hi)
    # m+1是因为pi是处于第k大
    if m + 1 == k:
        return pi
    elif m < k:
        # 减1是因为要排除pi元素
        return select(lo, k - m - 1)
    else:
        return select(hi, k)


# 插入排序
def insert_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            # 将元素向前挪
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums


# 递归版插入排序
def insert_sort_rec(nums, i):
    # 一直递归到最开始
    if i == 0:
        return
    insert_sort_rec(nums, i - 1)
    j = i
    while j > 0 and nums[j] < nums[j - 1]:
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        j -= 1
    return nums


# 选择排序
def select_sort(nums):
    # 选择目前最大的数，放在右边，从右边向左边遍历
    for i in range(len(nums) - 1, 0, -1):
        max_j = i
        for j in range(i):
            if nums[j] > nums[max_j]:
                # 记录当前最大的数，随时更新max_j
                max_j = j
        # 最后得出就是整体最大的数
        nums[i], nums[max_j] = nums[max_j], nums[i]
    return nums


# 递归版选择排序
def select_sort_rec(nums, i):
    if i == 0:
        return
    max_j = i
    for j in range(i):
        if nums[j] > nums[max_j]:
            max_j = j
    # 将最大数放在i的位置
    nums[i], nums[max_j] = nums[max_j], nums[i]
    # 递归去完成剩余的nums
    select_sort_rec(nums, i - 1)
    return nums


# 堆排序
def heap_sort(nums):
    from heapq import heappush, heappop
    h = []
    for num in nums:
        heappush(h, num)
    return [heappop(h) for i in range(len(h))]


# 冒泡排序
def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        # 一次外部迭代会确定一个最大数
        count = 0
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                count += 1
        # 如果没有一次交换，则说明已经有序
        if count == 0:
            break
    return nums


if __name__ == '__main__':
    array = [3, 2, 1, 5, 6, 4]
    res = Solution().findKthLargest(array, 2)
    print(res)
    print(merge_sort(array))
    print(select(array, 2))
    print(insert_sort(array))
    print(insert_sort_rec(array, len(array) - 1))
    print(select_sort(array))
    print(select_sort_rec(array, len(array) - 1))
    print(heap_sort(array))
    print(quick_sort(array, 0, len(array) - 1))
    print(quick_sort1(array, 0, len(array) - 1))
    print(bubble_sort(array))
