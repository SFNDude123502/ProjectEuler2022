#include "CBP.h"
startMain
    int lis[100][2];
    print(oint,len(lis));
    for(int a=-999;a<1000;a++){
        for(int b=1000;b>=-1000;b--){
            int c=0;
            for(int n=1;n<=500;n++){
                if(isPrime(quadratic(n,a,b))){
                    c++;
                }
            }
            if (c==250){
                lis[len(lis)][0]=a;
                lis[len(lis)][1]=b;
                printf("%d    %d\n",lis[len(lis)][0],lis[len(lis)][1]);
            }
        }
    }
    for(int i=0;i<len(lis);i++){for(int j=0;j<2;j++){printf(iint,lis[i][j]);}printf("\n");}
endMain
