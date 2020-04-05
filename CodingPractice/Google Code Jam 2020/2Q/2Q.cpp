#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string process(string s)
{
    string newS;

    char openBracket = '(';
    char closeBracket = ')';

    char openBracketCount = '0';
    char closeBracketCount = '0';

    for (int i = 0; i < s.length(); ++i)
    {
        char currentVal = s[i];

        char nextVal = s[i + 1];

        if (currentVal >= '0' && currentVal <= '9')
        {
            if (currentVal == '0')
            {
                newS.push_back(currentVal);
                continue;
            }

            else
            {
                while (openBracketCount < currentVal)
                {
                    newS.push_back(openBracket);
                    ++openBracketCount;
                }
                if (openBracketCount == closeBracketCount)
                {
                    openBracketCount = '0';
                    closeBracketCount = '0';
                }
                if ((i == (s.length() - 1)) && currentVal > 0)
                {

                    while (openBracketCount < currentVal)
                    {

                        newS.push_back(openBracket);
                        ++openBracketCount;
                        --currentVal;
                    }
                }
                newS.push_back(s[i]);
                if ((i != (s.length()) - 1) && currentVal > nextVal && nextVal == '0')
                {
                    if (currentVal == '1')
                    {
                        newS.push_back(closeBracket);
                        ++closeBracketCount;
                        continue;
                    }

                    while ((currentVal - '1') > 0)
                    {
                        newS.push_back(closeBracket);
                        ++closeBracketCount;
                        --currentVal;
                    }
                }
                if ((i != (s.length()) - 1) && currentVal > nextVal && nextVal != 0)
                {
                    while ((currentVal - '1') > 0)
                    {
                        newS.push_back(closeBracket);
                        ++closeBracketCount;
                        --currentVal;
                    }

                    continue;
                }

                else if (currentVal == nextVal)
                {
                    continue;
                }
                else if (currentVal < nextVal)
                {
                    newS.push_back(openBracket);
                    ++openBracketCount;
                    continue;
                }
                else
                {

                    while ((openBracketCount - closeBracketCount) > 0)
                    {
                        newS.push_back(closeBracket);
                        ++closeBracketCount;
                    }

                    if (openBracketCount == closeBracketCount)
                    {
                        break;
                    }
                }
            }
        }
    }

    s = newS;
    return s;
}

int main(int argc, char const *argv[])
{
    int T;
    cin >> T;

    for (int x = 1; x <= T; ++x)
    {
        string y; // String

        cin >> y;

        y = process(y);

        cout << "Case #" << x << ": " << y << "\n";
    }

    return 0;
}
