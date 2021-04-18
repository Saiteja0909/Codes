class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        arr=[-1]
        k=0
        l=0
        r=len(s)
        for i in range(len(s)-1):
            l=i
            for j in range(len(s)-1,i,-1):
                r=j
                if(s[l]==s[r]):
                    arr.append(r-l-1)
                    #break;
                elif(l==r or l==r-1):
                    arr.append(-1)
                    #break;
                else:
                    r-=1
        return(max(arr))
                    
