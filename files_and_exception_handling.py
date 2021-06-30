
# print(1/0) #ZeroDivisionError: division by zero


# we will create a file with required permission and see what errors/exception are possible to be seen
# first iteration
# file = open("order.text") # open() takes a string arg with file name
# print(file) # FileNotFoundError

# second iteration
try:
    file = open("order.text")
    print("file found") # try block required except or will throw an error
except FileNotFoundError as errmsg: # creating alias same as a nick name
    print(f"file not found! {errmsg}")
finally: #finally will execute regadless of try and except block execution, also used to clean up the code
    print("Thank you for visiting, See you again!")

# Let's create a file called orderr.text - naming is essential so ensure that it has the same name as above

# Let's apply DRY - OOP - Python packaging
        #      1     2          3
#hint 1 function
#2 create a class to put funciton into :
