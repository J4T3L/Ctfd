#include <stdio.h>
#include <string.h>

int main() {
    char key[64];
    printf("Enter Activation Key: ");
    scanf("%63s", key);
    if (strcmp(key, "SUP3R_S3CR37_K3Y_2026") == 0) {
        printf("Access Granted! Flag: CTF{r3v3rs3_3ng1n33r1ng_m4s73r_2026}\n");
    } else {
        printf("Access Denied!\n");
    }
    return 0;
}
