#1
#There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data." 
# Let's see if you can write a function to help clean US zip code data. 
# Given a string, it should return whether or not that string represents a valid zip code. For our purposes, a valid zip code is any string consisting of exactly 5 digits.
#HINT: str has a method that will be useful here. Use help(str) to review a list of string methods.

def is_valid_zip(zip_code):
    return len(zip_code) == 5 and zip_code.isdigit()

#print([is_valid_zip('12345')
#    ,is_valid_zip('1234x')
#    ,is_valid_zip('1234')
#    ,is_valid_zip('123456')
#    ,is_valid_zip('')
#    ,is_valid_zip('/n')])


