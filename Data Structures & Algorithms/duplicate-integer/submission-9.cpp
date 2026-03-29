class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int>numsSet;
        for(int i = 0;i < nums.size();i++){
            if(numsSet.count(nums[i])){
                return true;
            }
            numsSet.insert(nums[i]);
        }
        return false;
    }
};