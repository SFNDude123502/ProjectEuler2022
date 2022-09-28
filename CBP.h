
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#define oint "%d\n"
#define ostr "%s\n"
#define opos "%i\n"
#define odbl "%d\n"
#define oflt "%f\n"
#define olong "%ld\n"
#define ochar  "%c\n"
#define optr "%p\n"
#define ooct  "%o\n"
#define ohex "%x\n"
#define onull "%n\n"
#define olld "%lld\n"

#define iint "%d"
#define istr "%s"
#define ipos "%i"
#define idbl "%d"
#define iflt "%f"
#define ilong "%ld"
#define ichar "%c"
#define iptr "%p"
#define ioct "%o"
#define ihex "%x"
#define inull "%n"
#define illd "%lld"

#define startMain int main(){
#define endMain return 0;}

#define input(type, var) scanf(type, var)
#define prin(text) printf(text)
#define print(type,text) printf(type, text)

#define singleAllocateBytes(size) malloc(size)
#define arrayAllocateBytes(amount, bytesPer) calloc(amount, bytesPer)

#define len(arrPointer) (sizeof(arrPointer) / sizeof(arrPointer[0]))
long quadratic(int x,int a,int b){ return (x*x+a*x+b);}

bool isPrime(int num){for(int c=2;c<((int)num/2)+1;c++){if (num%c==0){return false;}}return true;}
