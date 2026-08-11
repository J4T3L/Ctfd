#include <stdio.h>
#include <stdlib.h>

void win() {
    printf("Flag: CTF{b0f_r372w1n_st4ck_0v3rwr173_2026}\n");
}

void vuln() {
    char buffer[64];
    printf("Enter input: ");
    gets(buffer); // Vulnerable to Stack Buffer Overflow!
}

int main() {
    vuln();
    return 0;
}
