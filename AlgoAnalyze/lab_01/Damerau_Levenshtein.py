def damerau_levenshtein(s1, s2):
    rows = len(s1) 
    cols = len(s2) 

    preprs = None
    precur = [x for x in range(cols + 1)] 
    cur = [1]  

    for i in range(1, rows + 1):  
            for j in range(1, len(precur)):    
                    if j > 1 and i > 1: 
                            correct = min(precur[j] + 1, 
                                                    cur[j - 1] + 1,
                                                    precur[j - 1] + 1, 
                                                    preprs[j - 2] + 1)

                            incorrect = min(precur[j] + 1,  
                                                            cur[j - 1] + 1,
                                                            precur[j - 1],
                                                            preprs[j - 2] + 1)

                            cur.append(correct) if s1[i - 1] != s2[j - 1] else cur.append(incorrect)

                    else:
                            correct = min(precur[j] + 1, 
                                                    cur[j - 1] + 1,
                                                    precur[j - 1] + 1)
                    
                            incorrect = min(precur[j] + 1, 
                                                            cur[j - 1] + 1,
                                                            precur[j - 1])

                            cur.append(correct) if s1[i - 1] != s2[j - 1] else cur.append(incorrect)

                    preprs = precur
                    precur = cur 
                    cur = [i + 1]
return precur[-1]
