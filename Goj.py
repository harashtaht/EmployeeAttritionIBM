# No 1
# 
# # arr = [5,7,8,3]

# i = 0
# s = 0

# while i<len(arr):
#     s = s+arr[i]
#     i = i+1
#     print('i',i, 's', s)

# No 2

# arr1 = [11,10,10,5,10,15,20,10,7,11]

# def foo(arr1, int_a, int_b, int_i, int_j):
#     k = int_j
#     ct = 0
#     while k > int_i-1:
#         if (arr1[k] <= int_b) and not (arr1[k] <= int_a):
#             ct += 1
#             break
#         k = k-1
#         break
#     return ct

# print(foo(arr1, 8, 18, 3, 6))
# print(foo(arr1, 10, 20, 0, 9))
# print(foo(arr1, 8, 18, 6, 3))
# print(foo(arr1, 20, 10, 0, 9))
# print(foo(arr1, 6, 7, 8, 8))

# No 3

# string = "fruits"

# print(string[1])

# def g(str):
#     i = 0
#     new_str = ""
#     while i<(len(str)-1):
#         new_str = new_str+str[i+1]
#         i += 1
#     return new_str

# def f(str):
#     if len(str) == 0:
#         return ""
#     elif len(str) == 1:
#         return str
#     else:
#         return f(g(str)) + str[0]

# def h(int_n, str_string):
#     while int_n != 1:
#         if int_n %2 == 0:
#             int_n = int_n/2
#         else:
#             int_n = (3*int_n) +1
#         str_string = f(str_string)
#     return str_string

# def powe(int_x, int_y):
#     if int_y == 0:
#         return 1
#     else:
#         int_x = int_x * powe(int_x, int_y-1) 
        

# print(h(1,"fruits"))
# print(h(2,"fruits"))
# print(h(5,"fruits"))
# print(h(powe(2, 1000000000000000), "fruits"))
# print(h(powe(2, 9831050005000007), "fruits"))

## No 4

# A, B, K
# Each test case has three numbers A, B, K

# Number of test cases T -> First line
# Output: Case C: X
# Where C is the case number (starting from 1)
# X is how many number divisible by K between A and B

# Constraints:
# 1<= T <= 100
# 1<= A <=B <10000
# 1<= K < 10000

#Sample Input
# 2 -> Number of test cases T (2 Times test)
# 1 -> A
# 10 -> B
# 3 -> K
# 8 -> A
# 20 -> B
# 4 -> K

num_T = input()

print(num_T)
print(type(num_T))

# def divisive(num_T):
#     loop = 0
#     for x in range(1, num_T+1, 1):
#         loop += 1
#         # print(f"Case {loop_case} is 5")
#         # print("Case", loop_case)
#     return loop, num_T

# print(divisive(num_T))

# for i in range(1, num_T+1, 1):
#     # print(f"Case {i}: 3")
#     print("Case ",i)

# for i in range(num_T):
#     # print(f"Case {}: {}.".format(i, num_T+1)
#     print(f'{i}')