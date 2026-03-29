class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet;
        unordered_map<int,int> seq;
        int longest = 0;
        if(nums.size() == 0){
            return 0;
        }
        for(int i = 0;i < nums.size();i++){
            numSet.insert(nums[i]);
        }
        //checking whether start sequence exists or not
        for(int i = 0;i < nums.size();i++){
            if(!numSet.count(nums[i] - 1)){
                //it is a start sequence
                int length = 0;
                while(numSet.count(nums[i] + length)){
                    length += 1;
                }
                longest = max(length, longest);
            }
        }
        return longest;
    }
};
