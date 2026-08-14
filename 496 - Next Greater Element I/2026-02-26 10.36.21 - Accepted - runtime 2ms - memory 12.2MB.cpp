
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        std::vector <int> res;
        
        for(int i=0;i<nums1.size();i++)
        {
            int Ft=-1;
            for(int j=0;j<nums2.size();j++)
            {
                if(nums1[i]==nums2[j])
                {
                    Ft=j;
                    break;
                }
            }
            int nextGreater=-1;
            for(int j=Ft+1;j<nums2.size();j++)
            {
                if(nums2[j]>nums1[i])
                {
                    nextGreater=nums2[j];
                    break;
                }
            }
            res.push_back(nextGreater);

        }
        return res;
        
    }
};