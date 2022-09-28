#include "CBP.h"

void euler12(){
    long long se=0;long long temp=0;
    for(int i=1;i<1000000;i++){
        se+=i;temp=0;
        for(int j=1;j<(int)(se/2)+1;j++){if(se%j==0){temp++;}}
        printf("\nTri: %d",i);printf(" Divis: %lld",temp);printf(" Value: %lld",se);
        if(temp>=500){printf(oint,i);printf(olld,se);break;}
    }
}

startMain
euler12();
endMain