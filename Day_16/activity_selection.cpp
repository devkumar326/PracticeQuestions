#include<bits/stdc++.h>
using namespace std;
bool myCmp(pair<int, int> a, pair<int, int> b)
{
    return a.second < b.second;
}

int activitySelection(int start[], int end[], int n){
    vector<pair<int, int>> jobTime;
    
    for(int i = 0; i < n; i++) {
        jobTime.push_back({start[i], end[i]});
    }
    
    sort(jobTime.begin(), jobTime.end(), myCmp);

    int count = 1;
    pair<int, int> last = jobTime[0];
    
    for(int i = 1; i < n; i++)
    {
        if(jobTime[i].first >= last.second)
        {
            count++;
            last = jobTime[i];
        }
    }
    
    return count;
}

int main() {
    int t;
    
    //testcases
    cin >> t;
    while(t--)
    {
        //size of array
        int n;
        cin >> n;
        int start[n], end[n];
        
        //adding elements to arrays start and end
        for(int i=0;i<n;i++)
            cin>>start[i];
        for(int i=0;i<n;i++)
            cin>>end[i];
        
        //function call
        cout << activitySelection(start, end, n) << endl;
    }
    return 0;
}