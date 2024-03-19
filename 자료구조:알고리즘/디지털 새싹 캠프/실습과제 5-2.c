#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

#define MAX_SIZE 100

typedef struct{
    int data[MAX_SIZE];
    int top;
} Stack;

void initialize(Stack* stack) {
    stack->top == -1;
}

int isEmpty(Stack* stack) {
    return stack ->top == -1;
}

int isFull(Stack* stack){
    return stack->top == MAX_SIZE - 1;
}

void push(Stack* stack, int value){
    if (isFull(stack)) {
        printf("Error: Stack is full.\n");
        exit(1);
    }

    stack->data[++stack->top] = value;
}

int pop(Stack* stack) {
    if (isEmpty(stack)) {
        printf("Error: Stack is empty.\n");
        exit(1);
    }

    return stack->data[stack->top--];
}

int calculate_postfix(char** expression, int size) {
    Stack stack;
    initialize(&stack);

    for (int i = 0; i < size; i++){
        char* token = expression[i];
    
        if (isdigit(token[0])) {
            push(&stack, atoi(token));
        } else{
            int operand2 = pop(&stack);
            int operand1 = pop(&stack);
        
            switch  (token[0]) {
            case '+':
                push(&stack, operand1 + operand2);
                break;
            case '-':
                push(&stack, operand1 - operand2);
                break;
            case '*':
               push(&stack, operand1 * operand2);
                break;
            case '/':
                push(&stack, operand1 / operand2);
                break;
            default: 
                printf("Error: Invalid operator.\n");
                exit(1);   
            }
        }
    }

    return pop(&stack);
}

int main(){
    char input[100];
    fgets(input, sizeof(input), stdin);

   char *expression[MAX_SIZE];
   char *token = strtok(input, " ");

    int count = 0;

    while (token != NULL && count < MAX_SIZE) {
        expression[count++] = token;
        token = strtok(NULL, " ");
    }

    int result = calculate_postfix(expression, count);

    printf("%d\n", result);

    return 0;
}