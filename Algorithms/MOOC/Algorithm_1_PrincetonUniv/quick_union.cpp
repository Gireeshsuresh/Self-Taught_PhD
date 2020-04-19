#include <iostream>
#include <vector>

using namespace std;

class QuickUnion
{
private:
    vector<int> id;
    int root(int i);

public:
    QuickUnion(int N);
    ~QuickUnion();
    bool connected(int p, int q);
    void unionPQ(int p, int q);
    void displayOutput();
};

QuickUnion::QuickUnion(int N)
{

    id.resize(N); /// Resize the Vector to User Input size.

    for (int i = 0; i < N; ++i)
    {
        id[i] = i;
    }
}

QuickUnion::~QuickUnion()
{
}

int QuickUnion::root(int i)
{
    while (i != id[i])
    {
        i = id[i];
    }
    return i;
}

/**
 * @brief Check to see if two nodes in an array are connected (i.e) Both the Index values retain the same value
 * 
 * @param p 
 * @param q 
 * @return true 
 * @return false 
 */
bool QuickUnion::connected(int p, int q)
{
    bool out = (id[p] == id[q]);
    cout << "Is ( " << p << " , " << q << " ) Connected ?? : " << out << "\n";
    return out;
}

/**
 * @brief unionPQ(int p, int q) sets id[p] equal to id[q].
 * 
 *        Any value in the array which has value equal to id[p] has to be replaced with id[q]
 * 
 * @param p The Entry (or) Index of the value to be replaced
 * @param q The Entry (or) Index of the value to be replaced With
 */
void QuickUnion::unionPQ(int p, int q)
{
    int i = root(p);
    int j = root(q);

    id[i] = j;
}

void QuickUnion::displayOutput()
{
    cout << "Output value of Array = | ";
    for (int i : id)
    {
        cout << i << " | ";
    }
    cout << "\n";
}

int main(int argc, char const *argv[])
{
    int N = 0; /// Take the User Input for the size of the array
    cout << "\nEnter the Size of the Array = ";
    cin >> N;
    cout << "\n";

    QuickUnion qfObject(N);

    qfObject.unionPQ(4, 3);
    qfObject.unionPQ(3, 8);
    qfObject.unionPQ(6, 5);
    qfObject.unionPQ(9, 4);
    qfObject.unionPQ(2, 1);
    qfObject.connected(8, 9);
    qfObject.connected(5, 0);
    qfObject.unionPQ(5, 0);
    qfObject.unionPQ(7, 2);
    qfObject.unionPQ(6, 1);
    qfObject.unionPQ(7, 3);


    cout << "\n";

    qfObject.displayOutput();

    cout << "\n";

    return 0;
}
