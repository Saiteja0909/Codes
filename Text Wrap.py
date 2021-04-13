def wrap(string, max_width):
    l=int(len(string)/max_width)
    m=len(string)-l*max_width
    ans=[]
    for i in range(0,l*max_width,max_width):
        ans.append(string[i:max_width+i])
        ans.append('\n')
    ans.append(string[i+max_width:i+max_width+m])
    ans=''.join(ans)
    return(ans)
