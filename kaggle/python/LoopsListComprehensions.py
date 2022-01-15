#1 
# Have you ever felt debugging involved a bit of luck? The following program has a bug. 
# Try to identify the bug and fix it.

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False

#print (has_lucky_number([0, -1, 7]))
#print (has_lucky_number([]))

#2
#R and Python have some libraries (like numpy and pandas) 
# compare each element of the list to 2 (i.e. do an 'element-wise' comparison) and give us a list of 
# booleans like `[False, False, True, True]`. 

#Implement a function that reproduces this behaviour, returning a 
# list of booleans corresponding to whether the corresponding element is greater than n.


#def elementwise_greater_than(L, thresh):
#   """Return a list with the same length as L, where the value at index i is 
#   True if L[i] is greater than thresh, and False otherwise.
    
#   >>> elementwise_greater_than([1, 2, 3, 4], 2)
#   [False, False, True, True]

def elementwise_greater_than(L, thresh):
    return [el>thresh for el in L]


#print(elementwise_greater_than([1, 2, 3, 4], 2))


#3
#Complete the body of the function below according to its docstring.

def menu_is_boring(meals):
	for i in range(1,len(meals)):
		if meals[i] == meals[i-1]:
			return True
		i+=1
	return False
	
print(menu_is_boring(['Spam', 'Eggs', 'Bacon', 'Spam']))