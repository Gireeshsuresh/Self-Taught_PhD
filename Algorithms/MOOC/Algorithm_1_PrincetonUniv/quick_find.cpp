#include <iostream>
#include <vector>

using namespace std;

class QuickFind
{
private:
    vector<int> id;

public:
    QuickFind(int N);
    ~QuickFind();
    bool connected(int p, int q);
    void unionPQ(int p, int q);
};

QuickFind::QuickFind(int N)
{
    for (int i = 0; i < N; ++i)
    {
        id[i] = i;
    }
}

QuickFind::~QuickFind()
{
}

/**
 * @brief Check to see if two nodes in an array are connected (i.e) Both the Index values retain the same value
 * 
 * @param p 
 * @param q 
 * @return true 
 * @return false 
 */
bool QuickFind::connected(int p, int q)
{
    return (id[p] == id[q]);
}

/**
 * @brief unionPQ(int p, int q) sets id[p] equal to id[q].
 * 
 *        Any value in the array which has value equal to id[p] has to be replaced with id[q]
 * 
 * @param p The Entry (or) Index of the value to be replaced
 * @param q The Entry (or) Index of the value to be replaced With
 */
void QuickFind::unionPQ(int p, int q)
{
    int pid = id[p];
    int qid = id[q];

    for (int i = 0; i < id.size(); ++i)
    {
        if (id[i] == pid)
        {
            id[i] == qid;
        }
    }
}

int main(int argc, char const *argv[])
{
    vector<int> userInput = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    return 0;
}
