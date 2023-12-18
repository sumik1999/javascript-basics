class Solution(object):


    def binsearch(self,num,arr):
        mid = len(arr) // 2
        if mid < len(arr) and mid >=0:
            if arr[mid] == num:
                print("found")
                return mid
            elif arr[mid] < num:
                return self.binsearch(num,arr[mid+1:])
            elif arr[mid] > num:
                return self.binsearch(num,arr[:mid])
        return -1

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_ind = {}
        for ind in range(len(nums)):   #---> O(n)
                hash_ind[nums[ind]] = ind    #will have the latest index for a repeated number
        result = []
        
        for ind in range(0,len(nums)):      #---> O(n)
            tar = target - nums[ind]

            if tar in hash_ind and hash_ind[tar]!=ind:
                    result.append(ind)
                    result.append(hash_ind[tar])
                    break
        return result

nums = [3,2,4]
inst_a = Solution()
print(inst_a.twoSum(nums,6))



        