#include<stdio.h>
#include<string.h>
#include<cs50.h>

int main(){
    string name = get_string("what is your name :\n");
    printf("hello, %s\n",name);
}
