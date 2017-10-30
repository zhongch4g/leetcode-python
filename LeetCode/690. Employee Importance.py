#-*-coding:utf-8 -*-
"""
    # @File    : 690. Employee Importance.py
    # @Author  : zhongch4g
    # @Time    : 2017/10/30 20:15
"""

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
"""
Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # idx = id - 1
        # val = employees[idx][1]
        # if employees[idx][2] is not None:
        #     for id in employees[idx][2]:
        #         val = val + self.getImportance(employees, id)
        #     return val
        # else:
        #     return employees[idx][1]




employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
employees1 = [[1,2,[2]], [2,3,[]]]
print(sorted(employees1, key = lambda x:x[0]))
id = 2
instance = Solution()
print(instance.getImportance(employees1, id))
