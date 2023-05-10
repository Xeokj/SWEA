#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

int a[11];
int b[11];
int c[11];

int main() {
    int test_case, T;
    int N, i, k;
    scanf("%d", &T);
    for (test_case = 1; test_case <= T; test_case++) {
        scanf("%d", &N);
        printf("#%d\n", test_case);
        a[1] = 1;
        for (k = 1; k <= N; k++) {
            for (i = 1; i < k; i++) {
                b[i] = a[i] + a[i - 1];
                c[i] = b[i];
                printf("%d ", b[i]);
            }
            for (i = 1; i < k; i++)
                a[i] = c[i];
            b[k] = 1;
            a[k] = b[k];
            printf("%d ", b[k]);
            printf("\n");
        }
    }
    return 0;
}