class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #dictionary impelmentation
        bindict={0:1}#binary dictionary declare
        cnt=0;s=0#initilize variables 
        #for i in range(len(nums)):
        for i in nums:#iterate nums array
            s+=i#incrementing the indx pos
            if s-k in bindict:cnt+=bindict[s-k]#checking nums[curr] and [next] pos values difference in binary dictionary and incrementing the count
            if s in bindict:bindict[s]+=1#checking the s is present in binarydictionary 
            else:bindict[s]=1#assigning the dictionary val to 1
        return cnt#printing count
