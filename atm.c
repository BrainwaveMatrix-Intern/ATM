#include <stdio.h>

int main() {
    int pin, enteredPin, attempts = 3;
    float balance = 1000.0, amount;
    int choice;

    pin = 1234;

    while (attempts > 0) {
        printf("Enter your 4-digit PIN: ");
        scanf("%d", &enteredPin);

        if (enteredPin == pin) {
            while (1) {
                printf("\n--- ATM MENU ---\n");
                printf("1. Check Balance\n");
                printf("2. Deposit Money\n");
                printf("3. Withdraw Money\n");
                printf("4. Exit\n");
                printf("Choose an option: ");
                scanf("%d", &choice);

                switch (choice) {
                    case 1:
                        printf("Current balance: $%.2f\n", balance);
                        break;
                    case 2:
                        printf("Enter amount to deposit: $");
                        scanf("%f", &amount);
                        if (amount > 0) {
                            balance += amount;
                            printf("Deposited: $%.2f\n", amount);
                        } else {
                            printf("Invalid amount.\n");
                        }
                        break;
                    case 3:
                        printf("Enter amount to withdraw: $");
                        scanf("%f", &amount);
                        if (amount > 0 && amount <= balance) {
                            balance -= amount;
                            printf("Withdrawn: $%.2f\n", amount);
                        } else {
                            printf("Invalid or insufficient funds.\n");
                        }
                        break;
                    case 4:
                        printf("Thank you for using the ATM.\n");
                        return 0;
                    default:
                        printf("Invalid choice.\n");
                }
            }
        } else {
            attempts--;
            printf("Incorrect PIN. Attempts left: %d\n", attempts);
        }
    }

    printf("Too many incorrect attempts. Exiting...\n");
    return 0;
}
