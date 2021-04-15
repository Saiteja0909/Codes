class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=list(s)
        s1=[]
        s2=[]
        k=0
        for i in range(len(s)):
            if(('a'<=s[i]<='z') or ('A'<=s[i]<='Z') or ('0'<=s[i]<='9')):
                s1.append(s[i])
        s1=''.join(s1)
        s1=s1.lower()
        s1=list(s1)
        #print(s1)
        s2=''.join(s1[::-1])
        s2=list(s2)
        #print(s2)
        return(s1==s2)
            
        
