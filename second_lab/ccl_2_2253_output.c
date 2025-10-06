#include <stdio.h>

int add(int a, int b) {
    return a + b; 
}

int multiply(int a, int b) {
    return a * b; 
}

int main() {
    int x = 5, y = 3; 

    
    int sum = add(x, y);
    
    
    int product = multiply(x, y);

    
    printf("Sum of %d and %d is %d\n", x, y, sum);
    printf("Product of %d and %d is %d\n", x, y, product);

    
    for (int i = 1; i <= 5; i++) {
        printf("Loop iteration: %d\n", i); 
    }

    return 0; 
}

