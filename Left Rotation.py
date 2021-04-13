def rotateLeft(d, arr):
    ans=[]
    for i in range(len(arr)):
        ans.append(arr[(i+d)%n])
    return(ans)
