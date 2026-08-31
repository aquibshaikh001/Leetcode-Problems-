#--------------------------------------------------------------------------
#Tried solving my way 



# target = int(input("Enter a target value : "))

# nums = []

# i = int(input("How many numbers you want to print"))

# for i in range(i):
#     a = int(input("Enter the numbers : "))
#     nums.append(a)

# sum = 0
# index = []
# print(nums)
# for index1,k in enumerate(nums):
#     n1 = k 
#     print("This is n1:",n1)
#     sum = n1
#     for index2,l in enumerate(nums):          # we use enumerate in loop to get the index of the elements 
#         if index2 >= 1:                #---------------------> This makes sure that we start the next number by 2nd index
#             n2 = l
#             sum = sum+n2 
#             if sum == target:
#                 index.append(index1)
#                 index.append(index2)
#                 break

# print(index)


# my_list = [10, 20, 30, 40, 50]
# counter = 0

# for num in my_list:
#     if counter == 1:
#         print(f"The second number by position is: {num}")
#         break
#     counter += 1



#-----------------------------------------------------------------------------------



# The final solution

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
