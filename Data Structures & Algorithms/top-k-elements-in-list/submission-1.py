class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        c={}
        output=[]
        count=0
        for i in range(n):
            if nums[i] not in c:
                c[nums[i]]=1
            if nums[i] in c:
                c[nums[i]]=c[nums[i]]+1
        reversed_by_values = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
        count=1
        for i in reversed_by_values.keys():
            output.append(i)
            if count==k:
                break
            count+=1
        return output


