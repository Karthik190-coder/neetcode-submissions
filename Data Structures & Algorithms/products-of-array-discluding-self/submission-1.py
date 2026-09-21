class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        total = math.prod(nums)
        n=len(nums)
        output=[]
        
        for i in range(n):
            if nums[i]==0:
                prod=1
                for j in range(n):
                    if i==j:
                        continue
                    prod*=nums[j]
                output.append(prod)
                continue
            output.append(int(total/nums[i]))
            
        return output
            
            

        