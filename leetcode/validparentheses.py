class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        starts = {"(":0,"{":1,"[":2}   #to have pairs
        ends = {")":0,"}":1,"]":2}
        
        latest_start=[]
        
        for item in s:
            if item in starts:           #store in start
                latest_start.append(item)
            elif latest_start:                #end is meaningful only if start exists and pop out if matches
                if ends[item] == starts[latest_start[-1]]:
                    latest_start.pop()
                else:
                    return False    #does not match false
            elif item in ends:      #ended without starting     
                return False


        if len(latest_start)>0:
            return False


        return True



            

inst_a = Solution()
print(inst_a.isValid("[["))