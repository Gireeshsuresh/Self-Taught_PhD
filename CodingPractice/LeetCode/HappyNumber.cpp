// Write an algorithm to determine if a number n is "happy".

// A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
// or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

// Return True if n is a happy number, and False if not.

// Example:

// Input: 19
// Output: true

// Explanation:
// (1)2 + (9)2 = 82
// (8)2 + (2)2 = 68
// (6)2 + (8)2 = 100
// (1)2 + (0)2 + (0)2 = 1

// Rough:
// 18 = 65 =61=37=58=89=145=42=20=4=16=37
// 14 = 17=50=25=29=85=89=145
// 28 = 68 =
// 37 =
// 46 = 52=29=85=89=
// 55 = 50

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <cstdlib>

using namespace std;

class Solution
{
public:
    bool isHappy(int n)
    {
        string s;

        s = to_string(n);
        unsigned int sz = s.size();
        unsigned int sum = 0;
        unsigned int num = 0;
        unsigned int count = 50;
        for (int iter = 0; iter < count; ++iter)
        {
            sum = 0;
            for (char c : s)
            {
                int temp = c - '0';
                sum += (temp * temp);
            }
            if (sum == 1)
            {
                return true;
            }
            else
            {
                s = to_string(sum);
            }
        }
        return false;
    }
};

int main(int argc, char const *argv[])
{
    int input = 10;

    Solution answer;

    bool output = answer.isHappy(input);

    cout << "\nOutput = " << output << "\n";

    return 0;
}