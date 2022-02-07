#Question 1 - 
def hello_name(user_name):
    print("hello_" + user_name +"!")
username = input("please enter your username:")
hello_name(username)

#Question 2 - define a function to create a list of odd numbers from 1 to 100
odds=[]
def first_odds(a,b):
    for values in range(a,b):
        if values%2 ==1:
            odds.append(values)
            return None


#Question 3 - Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    print(max(a_list))

rando_list = [15, 26456446, 6456, 465498746, 4657974]
max_num_in_list(rando_list)

#Question 4 - Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(year):
    if year % 4 == 0 and year % 100 ==0 and year % 400 == 0:
        print("True")
    elif year % 4==0 and year % 100 !=0:
        print("True")
    else:
        print("False")

is_leap_year (int(input("enter year here:")))




#Question 5 - Write a function to check to see if all numbers in list are consecutive numbers.

#find min and max of a_list
#create list(consec_list) containing range from min and max of a_list
#check if consec_list matches the sorted orignal list
consec_list=[]
def is_consecutive(a_list):
    minu=min(a_list)
    maxu=max(a_list)
    
    for values in range(minu,maxu):
        x = values
        consec_list.append(x)
        x=x+1

    if consec_list==sorted(a_list):
        print("True")
    else:
        print("False")
is_consecutive([6,4,2,3,1,5])    
