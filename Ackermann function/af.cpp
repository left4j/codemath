#include <cmath>
#include <iostream>

using std::cout;
using std::cin;
using std::endl;

int A (int m, int n)
{
    if(m == 0)
    {
        return n+1;
    }
    else if ((n == 0) && (m > 0))
    {
        return A(m-1, 1);
    }
    else if ((m > 0) && (n > 0))
    {
        return A(m-1, A(m, n-1));
    }
}

int main()
{
    int j;
    cout << "Enter m: ";
    cin >> j;
    int k;
    cout << "Enter n: ";
    cin >> k;
    cout << "Won't compute for A(4,2) and higher" << endl;
    // the longest int available in C++ is unsigned long long int which is only 2^64-2, while A(4,2) is 2^65533-3,
    // even boost library only allows for int1024_t, which is also just 2^1024-1, so even if stack overflow 
    // doesn't occur, cout will spit out a very wrong result, therefore it's better to leave A(m,n) as a simple int 
    // that will fail to compute for A(4,2) and anything above, but at least won't return an incorrect answer
    int AF;
    AF = A(j,k);
   
    cout << "Result: " << AF << endl;
    return 0;
}
