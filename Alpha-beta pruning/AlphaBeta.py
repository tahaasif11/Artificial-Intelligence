def Alpha_Beta(D,I,Turn,S,A,B):    
    if D == 3:  
        return S[I]
    if Turn:  
        Best = Beta 
        # Recur for left and right children  
        for i in range(0, 2):  
            V = Alpha_Beta(D+1,I*2+i,False,S,A,B)  
            Best = max(Best, V)  
            A = max(A,Best)  
            # Alpha Beta Pruning  
            if B <= A:  
                break
        return Best  
    else: 
        Best = Alpha 
        # Recur for left and right children  
        for i in range(0, 2):  
            V = Alpha_Beta(D+1,I*2+i,True,S,A,B)  
            Best = min(Best,V)  
            B = min(B,Best)  
            # Alpha Beta Pruning  
            if B <= A:  
                break 
        return Best
# Drive Code
# Initial values of Aplha and Beta  
Alpha, Beta = 1000, -1000 
Scores = [8,5,6,-4,3,8,4,-6,1,-3,5,2,-3,1,-2,5]
print("The optimal value is :", Alpha_Beta(0,0,True,Scores,Beta,Alpha))
