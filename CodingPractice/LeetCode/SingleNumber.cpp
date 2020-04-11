#include<iostream>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) 
    {
        sort(nums.begin(),nums.end());
        map<int,int> frequency;
        for(int i:nums)
        {
            frequency[i] = frequency[i]+1;
            // cout << "Frequency["<< i << "] = " <<frequency[i] << "\n";
            // cout << "nums = " << i << "\n\n";           
        }
        for (int i:nums)
        {
            if (frequency[i]==1)
            {
                return i;
            }
        }
        


        return 1;
    }
};

int main(int argc, char const *argv[])
{
    vector<int> input = {10,1,3,3,1,10,2};
    
    Solution answer;

    int output = answer.singleNumber(input);

    cout<<"Output = " << output << "\n";

    return 0;
}
