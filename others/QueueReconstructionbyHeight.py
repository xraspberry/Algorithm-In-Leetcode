'''

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
 where h is the height of the person and k is the number of people in front of this person who have a height greater
  than or equal to h. Write an algorithm to reconstruct the queue.

这道题的关键点在于要想清楚一件事情，就是比每个人大或者等于的都是比他高的或者一样高的，那么也就意味着我们的着手点就是从高到矮进行排列

这样每个人给的第二个元素就是在目前队列中的位置，以此类推，一直到最矮的，就可以拍好序了

Runtime: 145 ms
Your runtime beats 71.53 % of python submissions.
'''


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 先将最高的排出来，然后排次高的，以此类推
        from collections import defaultdict
        people_dict = defaultdict(list)
        for p in people:
            people_dict[p[0]].append(p)

        height = list(people_dict.keys())
        height.sort(reverse=True)

        res = []
        for h in height:
            # 从大到小，然后前面人的个数就是插入的位置
            # 相对于比其大或者等于人的位置
            people_dict[h].sort()
            for p in people_dict[h]:
                res.insert(p[1], p)

        return res