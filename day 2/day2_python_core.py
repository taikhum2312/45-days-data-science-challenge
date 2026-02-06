# Sum of numbers in a list
def sum_of_nums(input_list=input("enter a list of numbers seperated by coma")):
    total=0
    for nums in input_list.split(","):
        total+=int(nums)
    print("The sum of the numbers in list is:", total)
sum_of_nums()


# even_odd counter
def even_odd_counter(input_list=input("enter a list of numbers seperated by coma")):
    even_count=0
    even_numbers=[]
    odd_count=0
    odd_numbers=[]
    
    for nums in input_list.split(","):
        nums=int(nums)
        if nums % 2==0:
            even_count+=1
            even_numbers.append(nums)
        else:
            odd_count+=1
            odd_numbers.append(nums)
    print(f"Even numbers count: {even_count},  {even_numbers}")
    print(f"odd numbers count:  {odd_count},  {odd_numbers}")
even_odd_counter()

# second largest number in a list without sorting
def second_largest_num(input_list=input("enter a list of numbers seperated by coma")):
    largest=0
    second_largest=0
    for n in input_list.split(","):
        n=int(n)
        if n > largest:
            second_largest=largest
            largest=n
        elif n>second_largest and n!= largest:
            second_largest=n
    print(f"The Second largest number in the list is: {second_largest}")
second_largest_num()


# above_average numbers in a list

def above_average(nums):
    average= sum(nums) / len(nums)
    result=[]
    for n in nums:
        if n>average:
            result.append(n)
    print("Numbers above average:", result)
above_average(nums=[10,50,20,60,30,70,40,80])


# word frequency in a string



def word_frequency(sentence=input("enter a string")):
    frequency={}
    for word in sentence.lower().split():
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    print("Word frequency:", frequency)
word_frequency()


# most frequent word in a string
def most_frequent_word(sentence=input("enter a string")):
    frequency={}
    for word in sentence.lower().split():
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    most_frequent=max(frequency, key=frequency.get)
    print(f"The most frequent word is: '{most_frequent}' with frequency: {frequency[most_frequent]}")
most_frequent_word()

# merge two dictionaries
def merge_dict(d1,d2):
    result=d1.copy()
    for key in d2:
        if key in result:
            result[key]+=d2[key]
        else:
            result[key]=d2[key]
    print(f"merged dictionaries: {result}")
merge_dict({'a':1,'b':2}, {'b':3,'c':4})


sales = [1200, 1500, 800, 2000, 1800]
def total_sales(sales):
    total=0
    for sale in sales:
        total+=sale
    print(f"Total sales: {total}")
# total_sales(sales)

def average_sales(sales):
    average=sum(sales) / len(sales)
    print(f"Average sales: {average}")
# average_sales(sales)

def maximum_sales(sales):
    maximum=sales[0]
    for sale in sales:
        if sale>maximum:
            maximum=sale
    print(f"Maximum sales: {maximum}")
# maximum_sales(sales)

def minimum_sales(sales):
    minimum=sales[0]
    for sale in sales:
        if sale<minimum:
            minimum=sale
    print(f"Minimum sales: {minimum}")
# minimum_sales(sales)

## days above average sales
def above_average_sales(sales):
    average_sales=sum(sales) / len(sales)
    above_average=[]
    for sale in sales:
        if sale>average_sales:
            above_average.append(sale)
    print(f"Days with above average sales: {above_average}")
# above_average_sales(sales)

total_sales(sales)
average_sales(sales)
maximum_sales(sales)
minimum_sales(sales)
above_average_sales(sales)
