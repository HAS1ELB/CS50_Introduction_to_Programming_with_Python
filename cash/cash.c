#include<cs50.h>
#include<stdio.h>


int get_cents(void){
    int c;
    do{
        c =get_int("Cents Owed: ");
    }while (c < 0);
    return c;
}
int calculate_quarters(int cents){
    int q=0 ;
    while(cents >= 25){
        cents = cents - 25;
        q++;
    }
    return q;
}
int calculate_dimes(int cents){
    int d=0 ;
    while(cents >= 10){
        cents = cents - 10;
        d++;
    }
    return d;
}
int calculate_nickels(int cents){
    int n=0 ;
    while(cents >= 5){
        cents = cents - 5;
        n++;
    }
    return n;
}
int calculate_pennies(int cents){
    int p=0 ;
    while(cents >= 1){
        cents = cents - 1;
        p++;
    }
    return p;
}

int main(){
    int cents = get_cents();

    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    int pennies = calculate_pennies(cents);
    cents = cents - quarters * 25;

    int coins = quarters + dimes + nickels + pennies ;
    printf("%i\n",coins);
}
