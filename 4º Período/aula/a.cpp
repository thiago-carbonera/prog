#include <iostream>
using namespace std;

template <typename T>
void troca(T& a,T& b) {
    T aux;
    aux = a;
    a = b;
    b = aux;
}

int main() {
    int x = 2;
    int y = 0;

    troca(x, y);
    printf("x = %d \ny = %d\n", x, y);

    return 0;
}