class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest=0
        c=1
        newnums=set(nums) #no indexing in sets
        for i in newnums:
            if i-1 not in newnums: 
                #then i is the start of the sequence
                j=i
                c=1
                while (j+1 in newnums):
                    c+=1
                    j+=1
                if largest<c:
                    largest=c
        return largest

                    

            

