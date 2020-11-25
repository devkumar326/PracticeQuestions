#include<bits/c++.h>
using namespace std;
vector<long long> printFibb(int);



int main()
 {
     //taking total testcases
    int t;
    cin>>t;
    while(t--)
    {
        //taking number of elements
        int n;
        cin>>n;
        
        //calling function printFibb()
        vector<long long> ans = printFibb(n);
        
        //printing the elements of vector
        for(long long i:ans)cout<<i<<' ';
        cout<<endl;
    }
	return 0;
}

vector<long long> printFibb(int n) {
    long long int fib[n+1];
    fib[0]=fib[1]=1;
    if(n==1) {
        cout<<fib[0];
    }
    else if(n==2) {
        cout<< fib[0] <<" "<< fib[1]<<" ";
    }
    else {
        cout << fib[0] <<" "<< fib[1]<<" ";
        for(int i=2;i<n; i++) {
            fib[i]=fib[i-1]+fib[i-2];
            cout<< fib[i]<<" ";
        }
    }
}