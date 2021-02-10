# Write your code here
def contains_duplicates(xs):

    for i in range(0 , len(xs)):
        element = xs[i]
        for j in range(0, len(xs)):
            if(element == xs[j] and j is not i):
                return True
    return False

