#include <iostream>
#include <algorithm>
using namespace std;

int pos_maior (int*v, int ini, int fim) {
    int maior = ini;

    for (int i = ini+1; i <= fim; i++) {
        if(v[i] > v[maior]) {
            maior = i;
        }
    }
    return maior;
}

void selection_sort(int* v, int n) {
    for (int i = n-1; i > 0; i--) {
        int p = pos_maior(v, 0, i);
        std::swap(v[p], v[i]);
    }   
}

int main() {
    int v[] = {3,0,4,6,1,5,2};
    int n = 7;

    selection_sort(v,n);

    for (int i = 0; i < n; i++) {
        printf("%d ",v[i]);
    }
    printf(" \n");
    
    return 0;
}