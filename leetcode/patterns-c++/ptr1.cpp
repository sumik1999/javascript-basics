/**
 * * * * *
 * * * * *
 * * * * *
 * * * * *
 * * * * *
 */

#include <iostream>
// #include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, m;
    cout << "Enter the width : " << endl;
    cin >> n;
    cout << "Enter the height : " << endl;
    cin >> m;

    int a = 1;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << char(i + 25)
                 << " ";
            a += 1;
        }
        cout << endl;
    }
}
