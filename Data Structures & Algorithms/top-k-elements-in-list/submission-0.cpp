class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int>result;
        map<int,int>freqNumMap;
        for(int i = 0; i < nums.size();i++){
            freqNumMap[nums[i]]++;
        }
        vector<pair<int,int>>arr;
        for(auto it = freqNumMap.begin(); it != freqNumMap.end();it++){
            arr.push_back({it->second,it->first});
        }
        sort(arr.rbegin(),arr.rend());
        for(int i = 0;i < k;i++){
            result.push_back(arr[i].second);
        }
        return result;
    }
};
