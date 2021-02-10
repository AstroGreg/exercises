# Write your code here
def includes(xs, ys):

    for a in ys:
        if a not in xs:
            return False

    return True