#include<stdio.h>

int main() {
    int N, i = 1, j, cnt, temp;
    scanf("%d", &N);
    while (i <= N) {
        cnt = 0;
        temp = i;
        while (temp > 0) {
            if ((temp % 10) % 3 == 0 && (temp % 10) != 0)
                cnt++;
            temp /= 10;
        }
        if (cnt > 0) {
            for (j = 0; j < cnt; j++)
                printf("-");
            printf(" ");
            i++;
        }
        else
            printf("%d ", i++);
    }
    return 0;
}