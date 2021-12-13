#Fizz Buzz 
#Given a random number as an input to a function, return "FIZZ" if the number 
#is even and "BUZZ" if the number is odd
#Example Input: 1
#Example Output: 'BUZZ'
#Example Input: 1002
#Example Output: 'FIZZ'
#Collapse




#See video clips in action

def fizzbuzz(x):
    if x % 2 == 0:
        return "FIZZ"
    else:
        return "BUZZ"


print (fizzbuzz(1))
