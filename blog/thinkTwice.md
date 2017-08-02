刚才做了一道题，让我觉得算法非常重要，同样能够解决问题，写一个n2的算法相比较n的算法简直是灾难，而改变这一切只需要再考虑10秒钟，几行代码的事情，所以当遇到嵌套循环的时候，think twice

这道题目链接：[Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/)

O(n2)复杂度
========

刚开始时候的思路就是先遍历第一个list，然后每个元素再去第二个list查找，然后维护一个结果列表和最小和的值，总的时间复杂度是n2，因为遍历的复杂度是n，在列表中查找元素的复杂度是n，两者是嵌套关系，因此总的时间复杂度是n2

代码如下：

```
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
```

O(n)复杂度
===

但是转念一想，这样肯定有巨大的优化空间，因此查找位置这件事放在列表肯定不合适，那么在哪里呢，肯定是字典了，key为要查找的值，value是它的位置，这样查找位置的复杂度就是常数级了，那么整体的复杂度就是n了，但是这样会造成额外的空间使用，但是这又如何，我有16GB的内存呢

代码如下：

```
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
```

总结
===

所以啊，以后如果遇到嵌套循环，一定要三思，看这里面的循环能不能拿出来，只要能拿出来那就是对性能的巨大提升了！
