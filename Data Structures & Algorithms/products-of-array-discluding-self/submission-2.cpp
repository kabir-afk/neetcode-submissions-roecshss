class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int>res(n);
        vector<int>prev(n);
        vector<int>next(n);

        prev[0] = 1,next[n-1] = 1;
        for(int i = 1;i < n;i++){
            prev[i] = prev[i - 1] * nums[i - 1];
        }
        for(int i = n - 2;i >= 0;i--){
            next[i] = next[i + 1] * nums[i + 1];
        }
        for(int i = 0;i < n;i++){
            res[i] = prev[i] * next[i];
        }
        return res;
    }
};
