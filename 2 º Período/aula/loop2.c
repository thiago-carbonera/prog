#include <stdio.h>
void print_box (int lins, int cols){
    for (int i = 0; i < lins; i ++){
        for (int j = 0; j < cols; j ++){
            printf("🟥");
        }
        printf("\n");
    }
}

void print_left_triangle(int lins, int cols){
    for (int i = 0; i < lins; i ++){
        for (int j = 0; j <= i; j++){
            printf("🟥");
        }
        printf("\n");
    }
    printf("\n");
}

void print_right_triangle(int lins){
    for (int i = 0; i < lins; i ++){
        for (int j = 0; j < lins-i-1; j ++){
            printf("🟥");
        }
        for (int j = 0; j <= i; j++){
            printf("");
        }
        printf("\n");
    }
    printf("\n");
}

int main(){
    print_box(5,6);
    print_left_triangle(5,4);
    print_right_triangle(5);
    return 0;
}
