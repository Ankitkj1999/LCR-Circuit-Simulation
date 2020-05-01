#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<cstdlib>

using namespace std;
int main()
{   
    system("(color 7D)");
    float f=1000.0000,w,zc,c=0.00000507,wc,zl,l=2.0,r=10,i,p,a,b,c1,d;
    cout<<"Enter the value of Inducatance in H: ";
    cin>>l;
    cout<<"Enter the value of Capacitance in uF:";
    cin>>c;
    cout<<"Enter the value of Resiatance in ohm: ";
    cin>>r;
           cout<<"w                   zl             zc              f              i            zl-zc\n";

   for(f=1;f<=100;f++)
   {
      
       w=6.28*f;
       wc=w*c;
        zc=1/wc;
       zl=w*l;
       p=zl-zc;
       a=p*p;
       c1=r*r;
       b=a-c1;
       d=sqrt(b);
       i=100/d;
       cout<<w<<"\t  \t"<<zl<<"\t \t"<<zc<<"\t  \t"<<f<<"\t  \t"<<i<<"\t  \t"<<p<<endl;
       //cout<<i<<",";
        //f=f+199;

       
};
    //system("pwd");
    cout<<"\n\n";
    system("python test.py");

   return 0;
}
