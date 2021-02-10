# Write your code here

def is_prime(n):

    for i in range(n-1 , 1,-1):

        if(n % i == 0):
            return False

    if n is not 1:
     return True
    else:
        return False
is_prime(1)