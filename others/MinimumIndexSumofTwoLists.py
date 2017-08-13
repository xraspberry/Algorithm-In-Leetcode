'''

这道题 先遍历第一个列表，然后对于每一个元素在第二个列表中找，然后维护一个结果列表，和最小的和
遍历完成之后就得到答案了，错了一次，原因是没有想好最小和和结果列表的更新条件，

这样的时间复杂度是n2，遍历和查找
Runtime: 522 ms
Your runtime beats 23.13 % of python submissions.

'''


class SolutionA(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        minsum = len(list1) + len(list2)
        for index1, ele1 in enumerate(list1):
            try:
                index2 = list2.index(ele1)
            except ValueError as e:
                continue
            cursum = index1 + index2
            if cursum == minsum:
                res.append(ele1)
            elif cursum < minsum:
                minsum = cursum
                res = [ele1]

        return res


'''

可以进行优化，那就是将查找过程变成常数级的
首先将list2的元素和位置做成一个字典，这个是个n的操作
然后再遍历list1，这样在list2查找是常数级，遍历是n的操作，所以总体上也是n的操作
果然效率提高不少

Runtime: 115 ms
Your runtime beats 70.18 % of python submissions.

'''


class SolutionB(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        minsum = len(list1) + len(list2)
        cache2 = {}
        for index2, ele2 in enumerate(list2):
            cache2[ele2] = index2
        for index1, ele1 in enumerate(list1):
            index2 = cache2.get(ele1)
            if index2 is None:
                continue
            cursum = index1 + index2
            if cursum == minsum:
                res.append(ele1)
            elif cursum < minsum:
                minsum = cursum
                res = [ele1]

        return res
