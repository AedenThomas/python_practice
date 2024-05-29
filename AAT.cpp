#include <iostream>

using namespace std;
template <class T>
class ARRAY 
{
    public:
    T arr[5];
    void setdata()
    {
        for(int i=0;i<5;i++)
        {

            cout<<"enter any data to be put in the array that you want\n";
            cin>>arr[i];
            
        }
    }
    void getdata()
    {
        for(int i=0;i<5;i++)
        {
            cout<<arr[i];
        }
    }
};

int main()
{
    int b;
    cout<<"enter the following number to choose what type of array you want\n";
    cout<<"1. integer \n2. string \n3.float\n";
    cin>>b;
    cout<<b<<endl;

    
        ARRAY <int> a;

        ARRAY <float> d;
        ARRAY <string> c;




    switch (b)
    {
        case 1:
        a.setdata();
        a.getdata();
        break;
        
        case 2:
        c.setdata();
        c.getdata();
        break;
        
        case 3:
        d.setdata();
        d.getdata();
        break;
    
    default:
            cout<<"INVALID INPUT\n";
        break;
    }


    return 0;
}