#include <stdio.h>
#include <stdlib.h>

#define MAX_Q_SIZE 5
// 요소 타입 정의
typedef int element;

// 큐 구조체 정의
typedef struct {
    int front;
    int rear;
    element data[MAX_Q_SIZE];
} Queue;

// 오류 메시지 출력 함수
void error(char* message) {
    printf("%s\n", message);
    exit(0); // 프로그램 종료
}

// 큐 초기화 함수
void initQueue(Queue* q) {
    q->front = q->rear = -1;
}

// 큐가 가득 찼는지 확인하는 함수
int isFull(Queue* q) {
    return (q->rear == MAX_Q_SIZE - 1);
}

// 큐가 비어 있는지 확인하는 함수
int isEmpty(Queue* q) {
    return (q->front == q->rear);
}

// 큐에 요소를 추가하는 함수
void enQueue(Queue* q, element item) {
    if (isFull(q)) {
        printf("Queue is full.\n");
        return;
    }
    q->data[++q->rear] = item;
}

// 큐에서 요소를 제거하고 반환하는 함수
element deQueue(Queue* q) {
    if (isEmpty(q)) {
        printf("Queue is empty.\n");
        return 0; 
    }
    return q->data[++q->front];
}

// 큐를 출력하는 함수
void queuePrint(Queue* q) {
    int i;
    for (i = 0; i < MAX_Q_SIZE; i++) {
        if (i <= q->front || i > q->rear) {
            printf("%7c", '|');
        }
        else {
            printf("%4d%3c", q->data[i], '|');
        }
    }
    printf("\n");
}

int main() {
    element item = 0;
    Queue q;
    initQueue(&q);

    printf("\n");
    enQueue(&q, 10);
    queuePrint(&q);

    enQueue(&q, 20);
    queuePrint(&q);

    enQueue(&q, 30);
    queuePrint(&q);

    item = deQueue(&q);
    queuePrint(&q);

    item = deQueue(&q);
    queuePrint(&q);

    return 0;
}
