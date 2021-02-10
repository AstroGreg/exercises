def median(ns):
     list = sorted(ns)
     answer =  list[int(len(ns)/2)]
     if(len(ns)%2 == 0):
         return (list[int(len(ns)/2)] + list[int(len(ns)/2) - 1])/2
     return answer