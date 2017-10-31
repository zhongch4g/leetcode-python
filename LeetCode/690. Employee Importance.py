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
        # 没有考虑没有序号为1的情况
        # idx = id - 1
        # val = employees[idx][1]
        # if employees[idx][2] is not None:
        #     for id in employees[idx][2]:
        #         val = val + self.getImportance(employees, id)
        #     return val
        # else:
        #     return employees[idx][1]
        # index = [[employee.id, employee.importance, employee.subordinates] for employee in employees]
        # idx = id - 1
        # val = index[idx][1]
        # if index[idx][2] is not None:
        #     for id in index[idx][2]:
        #         val = val + self.getImportance(employees, id)
        #     return val
        # else:
        #     return index[idx][1]

        # 获得员工号对应员工对象的字典
        # empdict = {employee.id: employee for employee in employees}
        # val = 0
        # def dfs(id):
        #     if empdict[id].subordinates is None:
        #         return empdict[id].importance
        #     else:
        #         for sub in empdict[id].subordinates:
        #             val = val + dfs(sub)
        #     return val
        # return dfs(id)

        # answer online
        # emps = {employee.id: employee for employee in employees}
        #
        # # 深度优先搜索
        # def dfs(id):
        #     subordinates_importance = sum([dfs(sub_id) for sub_id in emps[id].subordinates])
        #     return subordinates_importance + emps[id].importance
        #
        # return dfs(id)







employees = [[[2,5,[]]]]
employees1 = [[1,2,[2]], [2,3,[]]]
print(sorted(employees, key = lambda x:x[0]))
id = 2
instance = Solution()
print(instance.getImportance(employees, id))
