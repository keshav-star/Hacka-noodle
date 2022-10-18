#include<iostream>
using namespace std;

int main()
{
int n,i,a[30],j,temp;

    //Array info
    cout<<"enter the number of elements:\n";
    cin>>n;

    cout<<"Enter the elements:\n";
    for(i=1;i<=n;i++)
    {
        cin>>a[i];
    } 
    
    for(i=1;i<=n-1;i++)
    {
        for(j=1;j<=n-i;j++)
        {
            if (a[j]>a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }
    cout<<"Array after sorting:\n";
    for(i=1;i<=n;i++)
    {
        cout<<" "<<a[i];
    }   
    return 0;
}
