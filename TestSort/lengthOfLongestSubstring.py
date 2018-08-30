class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_index = 0
        curr_index = 0
        curr_list=[]
        max_list=[]
        for p in s:#0,0
            if p not in curr_list:
                if(curr_index ==0 or curr_index==last_index+1):
                    curr_list.append(p)
                    print(curr_list)
                    last_index=curr_index; #0,0
            else:
                if(len(max_list)<=len(curr_list)):
                    print(curr_list)
                    max_list=curr_list
                    print(max_list)
                curr_list.clear()
            curr_index=curr_index+1;#1,0
        print(max_list)
        return len(max_list)

print(Solution.lengthOfLongestSubstring(1,"abcabcbb"))
