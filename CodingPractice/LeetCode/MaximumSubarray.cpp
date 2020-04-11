// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

// Example:

// Input: [-2,1,-3,4,-1,2,1,-5,4],
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.
// Follow up:

// If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int best = -2147483647;
        int sum = 0;
        for (int k = 0; k < nums.size(); ++k)
        {
            sum = max(nums[k], sum + nums[k]);
            best = max(best, sum);
        }
        return best;
    }
};

int main(int argc, char const *argv[])
{
    vector<int> input = {-1,0,56,2,2,-100};

    Solution answer;

    int output = answer.maxSubArray(input);

    cout << "\nOutput = " << output << "\n";

    return 0;
}