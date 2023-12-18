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