#include <algorithm>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <random>
#include <set>
#include <stack>
#include <vector>

using namespace std;

// BEGIN NO SAD
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef vector<int> vi;
// END NO SAD

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<vector<ll>> matrix;
typedef pair<ll, ll> pll;

// remember you may need to reset state
int g[105][105];
void rsolve() {
  int n;
  cin >> n;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      cin >> g[i][j];
    }
  }
  int ret = 0;
  int rr = 0;
  int cc = 0;
  for(int i = 0; i < n; i++) {
    ret += g[i][i];
    bool rrr = false;
    bool ccc = false;
    for(int j = 0; j < n; j++) {
      for(int k = 0; k < j; k++) {
        rrr |= g[i][j] == g[i][k];
        ccc |= g[j][i] == g[k][i];
      }
    }
    rr += rrr;
    cc += ccc;
  }
  cout << ret << " " << rr << " " << cc << "\n";
}

void solve() {
  int t;
  cin >> t;
  for(int casenum = 1; casenum <= t; casenum++) {
    cout << "Case #" << casenum << ": ";
    rsolve();
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  solve();
}
