#include <iostream>
#include <algorithm>
using namespace std;

inline int esq(int i) {
    return 2*i+1;
}

inline int dir(int i) {
    return 2*i+2;
}

void maxheapfy(int* v, int i, int th) {
    int e = esq(i), d = dir(i), maior = i;

    if((e < th) && (v[e] > v[i])) {
        maior = e;
    }

    if((d < th) && (v[d] > v[maior])) {
        maior = d;
    }

    if(maior != i) {
        std::swap(v[i], v[maior]);
        maxheapfy(v, maior, th);
    }
}


void buildmaxheap(int* v, int n) {
    for (int i = n/2; i >= 0; i--) {
        maxheapfy(v, i, n);
    }
}

void heapsort(int* v, int n) {
    buildmaxheap(v, n);

    for (int i = n-1; i > 0; i--) {
        std::swap(v[0], v[i]);
        maxheapfy(v, 0, i);
    }
}

