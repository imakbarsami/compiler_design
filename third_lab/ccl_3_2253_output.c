#include <stdio.h>  

int main() {
    int a = 5;       
    int b = 10;      
    int sum = a + b; 

    printf("Sum is: %d\n", sum); 

    if (sum > 10) {
        printf("Greater than 10\n"); 
    } else {
        printf("10 or less\n");
    }

    for (int i = 0; i < 5; i++) {
        printf("Count: %d\n", i); 
    }

    printf("int float return ");

    return 0; 
}

