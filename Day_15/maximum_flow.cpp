#include <bits/stdc++.h>
using namespace std;
bool bfs(vector<vector<int> > adj,vector<int> &vis,vector<int> &parent,int n,int u)
{
    queue<int>  q;
    q.push(u);
    vis[u]=1;
    while(!q.empty())
    {
       int i=q.front();
       q.pop();
       for(int j=0;j<adj.size();++j)
       {
           if(vis[j]==0&&adj[i][j]>0)
           {
               q.push(j);
               vis[j]=1;
               parent[j]=i;
               if(j==n)
              return true;
           }
          
       }
    }
    return false;
}
int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        vector<vector<int> > adj(n,vector<int> (n,0));
        int u,v,w;
        for(int i=0;i<m;++i)
        {
            cin>>u>>v>>w;
            adj[u-1][v-1]+=w;
            adj[v-1][u-1]+=w;
        }
       
        int max_flow=0;
        while(true)
        {
            vector<int> vis(n,0),parent(n,-1);
            if(bfs(adj,vis,parent,n-1,0)==false)
             break;
           
            int v=n-1,mx=INT_MAX;
            while(parent[v]!=-1)
            {
                mx=min(adj[parent[v]][v],mx);
                v=parent[v];
            }
            v=n-1;
            while(parent[v]!=-1)
            {
                adj[parent[v]][v]-=mx;
                adj[v][parent[v]]+=mx;
                v=parent[v];
            }
           
            max_flow+=mx;
        }
        cout<<max_flow<<endl;
    }
    return 0;
}