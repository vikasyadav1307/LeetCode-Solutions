class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        st_map={}
        for num in nums2:
            while stack and num > stack[-1]:
                st_map[stack.pop()]=num
            stack.append(num)

        while stack:
            st_map[stack.pop()]=-1
        
        result=[]
        for num in nums1:
            result.append(st_map[num])
        return result
        