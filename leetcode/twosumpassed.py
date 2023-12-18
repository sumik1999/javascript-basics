class Solution(object):


    def binsearch(self,num,arr):
        mid = len(arr) // 2
        if mid < len(arr) and mid >=0:
            if arr[mid] == num:
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
        for ind in range(len(nums)):
            if nums[ind] in hash_ind:
                hash_ind[nums[ind]].append(ind)
            else:
                hash_ind[nums[ind]] = [ind]
        result = []
        
        for ind in range(0,len(nums)):
            tar = target - nums[ind]
            if tar in hash_ind:
                if (len(hash_ind[tar]) == 1) and (tar!=nums[ind]):
                    result.append(ind)
                    result.append(hash_ind[tar][0])
                    break
                elif (tar==nums[ind]) and len(hash_ind[tar])>1:
                    result.append(ind)
                    result.append(hash_ind[tar][1])
                    break
        return result



        