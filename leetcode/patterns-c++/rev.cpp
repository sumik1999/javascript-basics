
#include <iostream>
// #include <bits/stdc++.h>

using namespace std;
int main()
{
    int num, rev = 0;
    cin >> num;
    for (int i = num; i > 0; i /= 10)
    {
        rev = rev * 10 + i % 10;
    }
    cout << rev << endl;
    if (rev == num)
        cout << "true" << endl;
    else
        cout << "false" << endl;
}