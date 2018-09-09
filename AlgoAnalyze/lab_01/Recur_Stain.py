def Lrecursion(s1, s2):
    if s1 == "": return len(s2)
    
    if s2 == "": return len(s1)
    
    cost = 0 if s1[-1] == s2[-1] else 1
           
    result = min([Lrecursion(s1[:-1], s2) + 1,
               Lrecursion(s1, s2[:-1]) + 1, 
               Lrecursion(s1[:-1], s2[:-1]) + cost])

    return result
