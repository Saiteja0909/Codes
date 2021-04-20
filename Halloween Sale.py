def howManyGames(p, d, m, s):
    sum=0
    k=-1
    a=p
    while(sum<=s):
        k+=1
        sum=sum+a
        if(a-d>=m):
            a=a-d
        else:
            a=m
    return(k)
