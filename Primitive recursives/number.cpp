#include <cmath>
#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;

int main()
{
    int n = 1;
    cout << n << ":" << pow(n,n-1) << endl;
       
    for(int n = 1; 0<n; n++)
    {   
        cout << n+1 << ":" << pow(n+1,pow(n,n-1)) << endl;
        if (n == 9) break;
    }

    return 0;
}