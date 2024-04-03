#include<stdio.h>
#include<cs50.h>

int main(){
    int height;
    do{
        height = get_int("Enter height here :");
    }while (height < 1 || height > 8);

    for (int row = 0; row<height ; row++){
        for(int space = 0; space < height - row - 1; space ++){
            printf(" ");
        }

        for(int column = 0; column <= row; column ++){
            printf("#");
        }
        printf("  ");
        for(int column = 0; column <= row; column ++){
            printf("#");
        }
        printf("\n");
    }

}
