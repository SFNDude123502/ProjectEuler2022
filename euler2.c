#include "CBP.h"

void fib(long long n1,long long n2,int* cen){
printf("%lld\n",n1);
long long t=n1+n2;long long i1=n2;long long i2=t;*cen=*cen+1;
if(*cen<=92){fib(i1,i2,cen);}}

startMain
int c=0;long long s=0;long long e=1;int *ce=&c;
fib(s,e,ce);
endMain