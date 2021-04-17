class Solution:
    def modifyString(self, s: str) -> str:
        s=list(s)
        k=chr(ord('a'))
        for i in range(len(s)):
            if(i==len(s)-1):
                if(s[len(s)-1]=='?'):
                    if(s[len(s)-2]==k):
                        k=chr((ord(k)+1))
                        if(ord(k)>122):
                            k=chr(ord('a'))
                    s[i]=(k)
            if(s[i]=='?'):
                if(s[i-1]==k or s[i+1]==k):
                    k=chr((ord(k)+1))
                    if(ord(k)>122):
                            k=chr(ord('a'))
                    if(s[i-1]==k or s[i+1]==k):
                        k=chr((ord(k)+1))
                        if(ord(k)>122):
                            k=chr(ord('a'))
                s[i]=(k)
        
        s=''.join(s)
        return(s)
