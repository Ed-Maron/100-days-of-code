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
        else:
            return False