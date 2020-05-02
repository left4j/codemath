#include <cmath>
#include <iostream>
#include <sstream>
using namespace std;

int main()
{
    int n;
    cout << "Input an integer greater than or equal to 1: " ;
    cin >> n;
    cout << "Sequence starts: " << endl;
    cout << n << ":" << pow(n,n-1) << endl;
    string s = to_string(n);
    string p = to_string(n-1);
    string f = s+p;
    int g = stoi(f);
    for(int k = n; 0<k; k++)
    {   
        cout << k+1 << ":" << pow(k+1,pow(k,k)) << endl;
        if (k == g-1) break;
    }

    return 0;
}
