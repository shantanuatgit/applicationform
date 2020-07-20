#include<bits/stdc++.h>
using namespace std;
int main()
{
   // forward_list<int> l1;
    forward_list<int> flist2;
    flist2.assign({1,2,3});
    //l2.assign({4,5,6});
    for(int&i :flist2)
        cout<<i<<" ";
}
