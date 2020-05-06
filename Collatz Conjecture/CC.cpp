#include <iostream>

using namespace std;

int CoF(int n, int w = 1)
{
    if(n == 1)
    {
        cout << "Returned to 1, try again lol. " << "Took " << w << " steps to do that" << endl;
        return 1;
    }
    else if(n%2)
    {
        cout << "Odd" << endl;
        return CoF(3*n+1, ++w);
    }
    else
    {
        cout << "Even" << endl;
        return CoF(n/2, ++w);  
    }
}

int main()
{
    int n;
    cout << "Input a positive integer: ";
    cin >> n;
    CoF(n);
    
   return 0; 
}
    
