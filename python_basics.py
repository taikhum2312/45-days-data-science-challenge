# Python Basics – Day 1

## Problem 1: Reverse a String
def reverse_string(input_string=input ("Enter a string to reverse: ")):
    return_string= ""
    for char in input_string:
        return_string = char + return_string
    print(return_string)
    # return return_string
reverse_string()


## Problem 2: Check for Palindrome
def palindrome_checker(input_string=input("enter a string to check")):
    reversed_string=""
    for char in input_string:
        reversed_string= char + reversed_string
    if reversed_string== input_string:
        print("True,string is a palindrome")
    else:
        print("false,string is not a palindrome")
palindrome_checker()

## Fibonacci Series (n terms)
def fibonacci_series(n=int(input("Enter number of terms for Fibonacci series: "))):
    a=0
    b=1
    for i in range(n):
        print(a, end=" ")
        next_num= a+b
        a=b
        b=next_num
fibonacci_series()
