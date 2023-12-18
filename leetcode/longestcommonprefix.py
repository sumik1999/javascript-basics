class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = ""

        smallest = ""
        min = 999999
        for item in strs:
            if len(item) < min:
                min = len(item)
                smallest = item

        i = 0
        count = [0]*min
        while(i < min):
            for index in range(len(strs)):
                if strs[index][i] != smallest[i]:
                    continue
                else:
                    count[i]+=1

            if (count[i]==len(strs)):
                if (i>0) and count[i-1]==len(strs):
                    pre+=smallest[i]
                elif (i==0):
                    pre+=smallest[i]
                else:
                    return pre
                    
            i+=1

        return pre

        

        
            
                
                

            

        s