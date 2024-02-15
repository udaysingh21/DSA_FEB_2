# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and
# you may not use the same element twice. You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""O(n)/O(n)"""

def indices(nums,target):
    dicti={}

    for i in range(len(nums)):
        reqd=target-nums[i]
        if reqd in dicti:
            return [dicti[reqd],i]
        else:
            dicti[nums[i]]=i


if __name__=="__main__":
    nums=[2,7,11,15]
    target=9
    print(indices(nums,target))



























# You have two tables in an Employee Management System database: Employees and Departments.
# Employees table:
# EmployeeID (int)
# EmployeeName (varchar)
# DepartmentID (int)
# Salary (decimal)
# Departments table:
# DepartmentID (int)
# DepartmentName (varchar)
# The Employees table contains data on employees, including their ID, name, the ID of the department they belong to, and their salary.
# The Departments table contains department IDs and their corresponding names.
# Tasks:
# Write a SQL query to find the name and salary of the highest-paid employee in each department.
# Write a SQL query to find the department name that has the maximum number of employees.
# Write a SQL query to find employees who earn more than the average salary of all employees.

# select name from Employees where salary>avg(salary)
# SELECT EmployeeName, Salary
# FROM Employees
# WHERE Salary > (SELECT AVG(Salary) FROM Employees