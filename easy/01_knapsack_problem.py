#include <iostream>
#include <string>
using namespace std;

int max(int a, int b)
{
    return (a>b) ? a : b;
}

int main() {
	int T = 0;
	int N = 0;
	int W = 0;
	cin>>T;
	for(int t=0; t<T; t++)
	{
	    cin>>N;
	    cin>>W;
	    int arrValue[N];
	    int arrW[N];
	    for(int i=0; i<N; i++)
	    {
	        cin>>arrValue[i];
	    }
	    for(int i=0; i<N; i++)
	    {
	        cin>>arrW[i];
	    }
	    //cout<<knapSack(W, arrW, arrValue, N);
	    int arrResult[N+1][W+1];
	    for(int n=0; n<=N; n++)
	    {
	        for(int w=0; w<=W; w++)
	        {
	            if(n==0 || w==0)
	            {
	                arrResult[n][w] = 0;
	            }
	            else
	            {
	                if(arrW[n-1] > w)
	                {
	                    arrResult[n][w] = arrResult[n-1][w];
	                }
	                else
	                {
	                    arrResult[n][w] = max(arrValue[n-1]+arrResult[n-1][w-arrW[n-1]], arrResult[n-1][w]);
	                }
	            }
	        }
	    }
	    cout<<arrResult[N][W]<<endl;
	}
	return 0;
}