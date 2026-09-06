class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=0
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in t:
                x=t.index(s[i])
                c+=1
                t=t[:x:]+t[x+1::]


        if c==len(s):
            return True
        else:
            return False