//主要就是三个函数 heapInsert,heapify,heapsort
#include<bits/stdc++.h>
using namespace std;

const int MAXN = 100001;

int arr[MAXN];
int n;

inline void swap(int i,int j){
    int tmp = arr[j];
    arr[j] = arr[i];
    arr[i] = tmp;
}

// 向下调整大根堆
// 当前堆大小为 size
void heapify(int i,int size){
    int l = i*2 + 1;
    while(l<size){
        int best = (l+1<size&&arr[l+1]>arr[l])?l+1:l;
        best = (arr[best]>arr[i])?best:i;
        if(best==i) break;
        swap(i,best);
        i = best;
        l = i*2 + 1;
    }
}

void heapInsert(int i){
    while(arr[i]>arr[(i-1)/2]){
        swap(i, (i-1)/2);
        i = (i-1)/2;
    }
}
// 从顶到底建立大根堆，O(n * logn)
// 依次弹出堆内最大值并排好序，O(n * logn)
// 整体时间复杂度O(n * logn)
void heapSort1(){ 
    for(int i=0;i<n;i++){
        heapInsert(i);
    }
    int size = n;
    while(size>1){
        swap(0, --size);
		heapify(0, size);
    }
}

// 从底到顶建立大根堆，O(n)
// 依次弹出堆内最大值并排好序，O(n * logn)
// 整体时间复杂度O(n * logn)
void heapSort2(){ 
    for(int i=n-1;i>=0;i--){
        heapify(i,n);
    }
    int size = n;
    while(size>1){
        swap(0, --size);
		heapify(0, size);
    }
}