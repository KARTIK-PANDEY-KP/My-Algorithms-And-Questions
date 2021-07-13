#include<iostream>
using namespace std;
int insertion_sort(int len, int arr[])
{
    for(int i = 1;i<len;i++)
    {
        int temp = arr[i];
        int j = i;
        while(j>0 && arr[j-1]>temp)
        {
            arr[j] = arr[j-1];
            j = j-1;
        }
        arr[j] = temp;
    }
    for(int i = 0;i<len;i++)
    {
        cout<<arr[i];
    }
}

int main()
{
    int len;
    cin>>len;
    int arr[len];
    for(int i = 0;i<len;i++)
    {
        cin>>arr[i];
    }
    insertion_sort(len, arr);
}
