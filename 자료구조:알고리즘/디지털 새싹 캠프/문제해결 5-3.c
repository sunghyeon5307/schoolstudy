#include <stdio.h>
#include <stdlib.h>
#define STACK_SIZE 20

typedef char element;
//스택 구조체 작성
typedef struct {
	element data[STACK_SIZE];
	int top;
}Stack;

void initStack( Stack *s );
int isFull( Stack *s );
int isEmpty( Stack *s );
void push( Stack *s, element data );
element pop( Stack *s );

int main(){
	int i;
    Stack s;
	char str[20];
	printf("문자열 입력 : ");
	scanf("%s", str);
	//문자열을 입력받아 거꾸로 출력
	for(int i=0;i<strlen(str); i++) {
		push(&s, str[i]);
	}
	for(int i=0; i<strlen(str); i++) {
		printf("%c", pop(&s));
	}
}

void initStack( Stack *s ){
	s->top = -1;
}
int isFull( Stack *s ){
	if(s->top == STACK_SIZE-1)
		return 1;
	return 0;
}
int isEmpty( Stack *s ){
if(s->top == -1)
	return 1;
	return 0;
}
void push( Stack *s, element c ){
	if(isFull(s)) {
		printf("스택이 꽉 차있습니다.\n");
		return;
	}
	s->data[++s->top] = c;
}
element pop( Stack *s ){
	if(isEmpty(s)) {
		printf("스택이 비어있습니다.\n");
		return 0;
	}
	return s->data[s->top--];
}