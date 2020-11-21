#include<bitsc++.h>
using namespace std;

class FindMedian
{
	public:
		void insertHeap(int &);
		double getMedian();
	private:
		double median; //Stores current median
		priority_queue<int> max; //Max heap for lower values
		priority_queue<int, vector<int>, greater<int> > min; //Min heap for greater values
		void balanceHeaps(); //Method used by insertHeap
};

void FindMedian::insertHeap(int &x)
{
	if(max.empty() == true)
    {
        max.push(x);
        return;
    }
    
	if(max.size() > min.size())
	{
	    if(max.top() > x)
	    {
	        min.push(max.top());
	        max.pop();
	        max.push(x);
	    }
	    else
	    {
	        min.push(x);
	    }
	}
	else
	{
	    if(x < max.top())
	    {
	        max.push(x);
	    }
	    else
	    {
	        min.push(x);
	        max.push(min.top());
	        min.pop();
	    }
	}
}
double FindMedian::getMedian()
{
	if(max.size() > min.size())
	{
	    return max.top();
	}
	else
	{
	    return (max.top() + min.top())/2.0;
	}
}

int main()
{
    int n, x;
    int t;
    cin>>t;
    while(t--)
    {
    	FindMedian Ans;
    	cin >> n;
    	for(int i = 1;i<= n; ++i)
    	{
    		cin >> x;
    		Ans.insertHeap(x);
    	    cout << floor(Ans.getMedian()) << endl;
    	}
    }
	return 0;
} 