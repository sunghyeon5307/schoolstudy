#include <stdio.h>

typedef struct score{
    int kor, eng, mat;
    int total;
}Score;

int main(){
    int i;
    Score s[3] = {
        {50, 50, 50},
        {60, 60, 60},
        {70, 70, 70},
    };
Score *p = s;

for (int i = 0; i<3; i++)
{
    s[i].total = s[i].kor + s[i].eng + s[i].mat;
    (p+i) -> total = (p+i)->kor+(p+i)->eng+(p+i)->mat;
}
}