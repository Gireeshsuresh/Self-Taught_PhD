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

        while (1)
        {
            int result = 0;

            while (n != 0)
            {
                result += (n % 10) * (n % 10);
                n /= 10;
            }

            if (result == 1)
                return true;
            else if (result == 4)
                return false;
            n = result;
        }
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