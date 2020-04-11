
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int singleNumber(vector<int> &nums)
    {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        unsigned int res = 0;
        for (unsigned int i : nums)
        {
            res = res ^ i;
        }
        return res;
    }
};

int main(int argc, char const *argv[])
{
    vector<int> input = {10, 1, 3, 3, 1, 10, 2};

    Solution answer;

    int output = answer.singleNumber(input);

    cout << "Output = " << output << "\n";

    return 0;
}
