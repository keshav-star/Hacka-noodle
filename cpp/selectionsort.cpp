#include<iostream>
using namespace std;

int main()
{
    //declare variables
    int i,n,p,a[20],j,temp,min;
    //Get info about array
    cout<<"Enter the number of elements in array to be sorted :\n";
    cin>>n;

    cout<<"Enter the Array elements: \n";
    for(i=1;i<=n;i++)
    {
        cout<<"Enter "<<i<<"th element: ";
        cin>>a[i];
    }

    //1st loop 
    for(i=1;i<=n;i++)
    {
        min=a[i];
        p=i;
        for(j=i+1;j<=n;j++)
        {
            if(min>a[j])
            {
                min=a[j];
                p=j;
            }
        }
            if(p!=i)
            {
                temp=a[i];
                a[i]=a[p];
                a[p]=temp;
            }

    }
    cout<<"Sorted array is:\n";
    for(i=1;i<=n;i++)
    {
        cout<<a[i];
        cout<<" ";
    }


}
