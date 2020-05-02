#include <cmath>
#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter n: " << endl;
    cin >> n;
    cout << n << ":" << pow(n,n-1) << endl;
       
    for(int n = 1; 0<n; n++)
    {   
        cout << n+1 << ":" << pow(n+1,pow(n,n-1)) << endl;
        if (n == 9) break;
    }

    return 0;
}
