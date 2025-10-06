#include <stdio.h>  // standard input output
/*hello world
 my name is sami
*/
int main() {
    int a = 5;       // declare integer
    int b = 10;      // another variable
    int sum = a + b; // addition

    printf("Sum is: %d\n", sum); // print result

    if (sum > 10) {
        printf("Greater than 10\n"); // condition check
    } else {
        printf("10 or less\n");
    }

    for (int i = 0; i < 5; i++) {
        printf("Count: %d\n", i); // loop
    }

    printf("int float return ");

    return 0; // exit
}

