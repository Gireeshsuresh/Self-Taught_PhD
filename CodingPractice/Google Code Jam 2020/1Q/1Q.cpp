#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
int constexpr ArrSize = 100;

int findTrace(vector<vector<int>> &matrix)
{
    int sum = 0;
    for (int i = 0; i != matrix.size(); ++i)
    {
        for (int j = 0; j != matrix[i].size(); ++j)
        {
            if (j == i)
            {
                sum = sum + matrix[i][j];
            }
        }
    }
    return sum;
}

int rowrepeat(vector<vector<int>> &matrix)
{
    int count = 0;

    for (int i = 0; i != matrix.size(); ++i)
    {
        map<int, int> frequency;
        for (int p : matrix[i])
        {
            ++frequency[p];
            if (frequency[p] == 2)
            {
                ++count;
                break;
            }
        }
    }
    return count;
}

void transpose(vector<vector<int> > &b)
{
    if (b.size() == 0)
        return;

    vector<vector<int> > trans_vec(b[0].size(), vector<int>());

    for (int i = 0; i < b.size(); i++)
    {
        for (int j = 0; j < b[i].size(); j++)
        {
            trans_vec[j].push_back(b[i][j]);
        }
    }

    b = trans_vec;  
}
int main(int argc, char const *argv[])
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++)
    {
        int k = 0; // Trace
        int r = 0; // Row    Repeat
        int c = 0; // Column Repeat

        int N = 0; // Square Matrix Size

        cin >> N;
        vector<vector<int>> A(N, vector<int>(N));

        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < N; ++j)
            {
                cin >> A[i][j];
            }
        }

        k = findTrace(A);
        r = rowrepeat(A);
        transpose(A);
        c = rowrepeat(A);

        cout << "Case #" << t << ": " << k << " " << r << " " << c << "\n";
    }

    return 0;
}
