class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int>numsMap;
        for(int i = 0;i < nums.size();i++){
            numsMap[nums[i]] = i;
        }
        for(int i = 0;i < nums.size();i++){
            int difference = target - nums[i];
            if(numsMap.count(difference) && i != numsMap[difference]){
                return {i,numsMap[difference]};
            }
        }
        return {};
    }
};
