#include<iostream>
#include<climits>
using namespace std;
void show_me(int arr[],int n,int word_limit){
    int dp[n+1];
    dp[n] = 0;
    int ends_at[n];
    for(int curr_index = n-1;curr_index>=0;curr_index--){
        int cnt = 0;
        int sum = 0;
        dp[curr_index] = INT_MAX;
        ends_at[curr_index] = curr_index;
        for(int next_index = curr_index;next_index<n;next_index++){
            if(sum+cnt+arr[next_index]>word_limit){
                break;
            }else{
                int extra_spaces = next_index == n-1?0: word_limit-cnt-sum-arr[next_index];
                if(dp[curr_index]>dp[next_index+1]+extra_spaces*extra_spaces){
                    ends_at[curr_index] = next_index;
                    dp[curr_index]  = dp[next_index+1]+extra_spaces*extra_spaces;
                }
                cnt++;
                sum += arr[next_index];
            }
        }
    }
    int current_index = 0;
    while(current_index<n){
        cout<<current_index+1<<" "<<ends_at[current_index]+1<<" ";
        current_index = 1 + ends_at[current_index];
    }
}
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        
        cin>>n;
        int arr[n];
        int word_limit;
        
        for(int i=0;i<n;i++)
            cin>>arr[i];
        cin>>word_limit;
    
        show_me(arr,n,word_limit);
        cout<<endl;
    }
}
