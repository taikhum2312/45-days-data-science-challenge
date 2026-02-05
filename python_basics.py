# Python Basics – Day 1

# ## Problem 1: Reverse a String
# def reverse_string(input_string=input ("Enter a string to reverse: ")):
#     return_string= ""
#     for char in input_string:
#         return_string = char + return_string
#     print(return_string)
#     # return return_string
# reverse_string()


# ## Problem 2: Check for Palindrome
# def palindrome_checker(input_string=input("enter a string to check")):
#     reversed_string=""
#     for char in input_string:
#         reversed_string= char + reversed_string
#     if reversed_string== input_string:
#         print("True,string is a palindrome")
#     else:
#         print("false,string is not a palindrome")
# palindrome_checker()

# ## Fibonacci Series (n terms)
# def fibonacci_series(n=int(input("Enter number of terms for Fibonacci series: "))):
#     a=0
#     b=1
#     for i in range(n):
#         print(a, end=" ")
#         next_num= a+b
#         a=b
#         b=next_num
# fibonacci_series()

## count characters in a string
def count_characters(input_string=input("enter a string to count characters")):
    char_count={}
    for char in input_string:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    print(char_count)
count_characters()


## maximum in a list
def maximum_number(input_list=input("enter a list of numbers separated by commas: ").split(",")):
    max_num= float(input_list[0])
    for num in input_list:
        if float(num) > max_num:
            max_num= float(num)
    print("Maximum number is:", max_num)
maximum_number()

##prime number checker
def prime_checker(n=int(input("enter a number to check if it is prime: "))):
    if n <= 1:
        print("Not a prime number")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not a prime number")
            return
    print("Prime number")
prime_checker()
