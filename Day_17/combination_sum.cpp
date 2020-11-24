#include<bits/c++.h>
using namespace std;

void calSum(vector<int> A, int sum, vector<int> &temp, int index, vector<vector<int>> &res)
{
    if(sum == 0)
    {
        res.push_back(temp);
        return;
    }
    
    for(int i = index; i < A.size(); i++)
    {
        if(sum - A[i] >= 0)
        {
            temp.push_back(A[i]);
            sum = sum - A[i];
            
            calSum(A, sum, temp, i, res);
            
            sum = sum + A[i];
            temp.pop_back();
        }
    }
}

vector<vector<int> > combinationSum(vector<int> &A, int sum) {
    sort(A.begin(), A.end());
    A.erase(unique(A.begin(), A.end()), A.end());
    
    vector<vector<int>> res;
    vector<int> temp;
    
    calSum(A, sum, temp, 0, res);
    
    return res;
}

int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> A;
        for(int i=0;i<n;i++){
            int x;
            cin>>x;
            A.push_back(x);
        }   
        int sum;
        cin>>sum;
        vector<vector<int> > result;
   		result=combinationSum(A, sum);
   		if(result.size()==0){
   			cout<<"Empty";
   		}
        for(int i=0;i<result.size();i++){
            cout<<'(';
            for(int j=0;j<result[i].size();j++){
                cout<<result[i][j];
                if(j<result[i].size()-1)
                    cout<<" ";
            }
            cout<<")";
        }
        cout<<"\n";
    }
}