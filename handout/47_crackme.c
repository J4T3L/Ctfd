#include <stdio.h>
#include <string.h>

int main() {
    char key[64];
    printf("Enter Activation Key: ");
    scanf("%63s", key);
    if (strcmp(key, "SUP3R_S3CR37_K3Y_2026") == 0) {
        printf("Access Granted! Flag: CTF{c_3lf_cr4ckm3_gdb_2026}\n");
    } else {
        printf("Access Denied!\n");
    }
    return 0;
}
