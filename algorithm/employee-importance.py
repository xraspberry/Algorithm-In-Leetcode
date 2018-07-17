"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def traverse(self, employee_id):
        employee = self.employees_dict[employee_id]
        importance = employee.importance
        for subordinate in employee.subordinates:
            importance += self.traverse(subordinate)
        return importance

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.employees_dict = {e.id: e for e in employees}
        return self.traverse(id)


if __name__ == '__main__':
    employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    id = 1
    res = Solution().getImportance(employees, id)
    print(res)
    assert res == 11

