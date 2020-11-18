/*
Netkent University
Data Stuructures
Leson 01
Arrays
*/

#include <stdio.h>

int main() {
    float dizi[5];
    float ortalama, toplam=0;
    int i;

    for (int i = 0; i < 5; ++i) {
        printf("%2d. elemanı giriniz > ", (i+1));
        scanf("%f", &dizi[i]);
        toplam = dizi[i];
    }

    ortalama = toplam / 5.0;

    printf("Ortlama : %.2f\n", ortalama);

    return 0;
}
