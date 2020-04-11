
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution
{
public:
    void moveZeroes(vector<int> &nums)
    {
        int lastNonZeroFoundAt = 0;
        // If the current element is not 0, then we need to
        // append it just in front of last non 0 element we found.
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] != 0)
            {
                nums[lastNonZeroFoundAt++] = nums[i];
            }
        }
        // After we have finished processing new elements,
        // all the non-zero elements are already at beginning of array.
        // We just need to fill remaining array with 0's.
        for (int i = lastNonZeroFoundAt; i < nums.size(); i++)
        {
            nums[i] = 0;
        }
    }
};

void printOutput(vector<int> &nums)
{
    for (auto &&i : nums)
    {
        cout << i << " ";
    }
    cout << "\n";
}
int main(int argc, char const *argv[])
{
    vector<int> userInput = {0, 1, 0, 3, 12};

    Solution answer;

    answer.moveZeroes(userInput);

    printOutput(userInput);

    return 0;
}
