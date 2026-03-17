class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int n = nums.size();
        int first = INT_MAX;
        int second = INT_MAX;

        // Find an increasing subsequence of length 3
        for(int i=0; i < n; i++) {
            // Reduce the first as low as possible
            if(first >= nums[i])
                first = nums[i];
            // Has to be larger than the first, still reduce to the lowest possible
            else if(second >= nums[i])
                second = nums[i];
            // If a third value is found > the first and second we have a triplet
            else
                return true;
        }
        return false; // No increasing triplet is found in the array
    }
};