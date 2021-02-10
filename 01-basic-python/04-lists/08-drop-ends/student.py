# Write your code here
def drop_ends(xs):

   lol = xs.copy()
   lol.remove(xs[-1])
   lol.remove(xs[0])

   return lol