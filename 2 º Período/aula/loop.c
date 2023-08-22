#include <stdio.h>

int main(){
    int i = 0;

    while (i < 11){    // WHILE
        printf("%d ", i);
        i++; // também pode usar: i = +1
    }
    printf("\n");

    for (int i = 0; i < 10; i++){   // FOR
        printf("%d ", i);
    }
    return 0;
}

int main1(){
    printf("Informe inteiros (0 = sair):");
    int x = 1;
    int sum = 1;
    while (x != 0){
        sum *= x;
        if (x == 0) break;
        scanf(" %d", &x);
    }
    printf("Prod: %d\n", sum);
    return 0;
}
