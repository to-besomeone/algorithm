#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;

struct Item {
    int date;
    int page;
};

int maxpage;

bool cmp(Item a, Item b) 
{ 
	double r1 = (double)a.page / a.date; 
	double r2 = (double)b.page / b.date; 
	return r1 > r2; 
} 

bool promising(int n,int W, int i, int page, int date, Item arr[]){
    int j;
    int totdate;
    float bound;
    if(date >= W)
        return false;
    else{
        j = i+1;
        bound = page;
        totdate = date;
        while((j < n) && (totdate + arr[j].date <= W)){
            totdate += arr[j].date;
            bound += arr[j].page;
            j++;
        }
        if (j < n){
            bound += (W - totdate) * (arr[j].page / arr[j].date);
        }
        return bound > maxpage;
    }
}

void knapsack(int n, int W, int i, int page, int date, Item arr[]){
    if(date <= W && page > maxpage){
        maxpage = page;
    }
    if(promising(n, W, i, page, date, arr)){
        knapsack(n, W, i+1, page + arr[i+1].page, date+arr[i+1].date, arr);
        knapsack(n, W, i+1, page, date, arr);
    } 

}

int main(){
    int N, M;
    cin >> N >> M;

    Item* arr = new Item[M];
    // srand((unsigned)time(NULL));
    // W = rand()%2000+1;

    for(int i=0;i<M;i++){
		cin >> arr[i].date >> arr[i].page ;
	}

    sort(arr, arr + M, cmp);
    knapsack(M, N, -1, 0, 0, arr);
    cout << maxpage << endl;

}