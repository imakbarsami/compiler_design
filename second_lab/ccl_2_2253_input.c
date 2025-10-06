#include <stdio.h>
/* 
   This is a sample C program 
   that performs basic arithmetic 
   operations and prints the result
*/
/* Function to add two numbers */
int add(int a, int b) {
    return a + b; // returning the sum
}
/* Function to multiply two numbers */
int multiply(int a, int b) {
    return a * b; // returning the product
}
// Main function starts here
int main() {
    int x = 5, y = 3; // declaring and initializing variables

    // Performing addition
    int sum = add(x, y);
    
    // Performing multiplication
    int product = multiply(x, y);

    /* Displaying the results 
       using printf statement
    */
    printf("Sum of %d and %d is %d\n", x, y, sum);
    printf("Product of %d and %d is %d\n", x, y, product);

    // Loop to print numbers from 1 to 5
    for (int i = 1; i <= 5; i++) {
        printf("Loop iteration: %d\n", i); // printing each iteration
    }

    return 0; // End of program
}

