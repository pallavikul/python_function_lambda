# def hi():
#     return "hi"
# def hello(a):
#     return a
# a=hello(hi())
# print(a)

# anonymous  function
# b=lambda x: x+2
# print(b(10))

# a=lambda e:"even"if e%2==0 else "odd"
# print(a(5))

# def s(a)
#      for i in range(1, a+1 ,2):

# Calculate the sum of digits of a number using a while loop.
# e.g., 123 → 6
# def a(num):
#     sum=0
#     while num>0:
#         d=num%10  
#         sum=sum+d 
#         b=num//10 
#     return sum   
# print(a(123))  
def a(num):
    sum = 0
    while num > 0:
        d = num % 10      # get last digit
        sum = sum + d     # add digit to sum
        num = num // 10   # remove last digit (fix: update num, not b)
    return sum            # return after the loop ends

print(a(123))  # Output: 6

   

# Reverse a number using a while loop.
# e.g., 123 → 321
# def rev(num):
#     rev=0
#     while num>0:
#         a=num%10         # Get the last digit
#         rev=rev*10+a     # Append digit to reversed number
#         num=num//10      # Remove last digit from n
#     return rev  
# print(rev(123))


# ⚙ Intermediate Level
# Check if a number is a palindrome using a while loop.
# e.g., 121 → Palindrome
# def palindrome(num):
#     o=num
#     rev=0
#     while num>0:
#         a=num%10
#         rev=rev*10+a
#         num=num//10
#     return "palindrome" if 0==rev else "not palindrome"
# print(palindrome(121))

# 
