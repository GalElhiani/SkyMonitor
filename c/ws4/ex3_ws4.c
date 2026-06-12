/* This program lists and prints all of data types in c
File: ex3_ws4.h
Author: Gal Elhiani
Tester: Amir Malul
*/

#include <stdio.h>
#include <stdint.h>
#include <stddef.h>

int main() {
    printf("%-22s : %zu bytes\n", "char", sizeof(char));
    printf("%-22s : %zu bytes\n", "signed char", sizeof(signed char));
    printf("%-22s : %zu bytes\n", "unsigned char", sizeof(unsigned char));

    printf("%-22s : %zu bytes\n", "short", sizeof(short));
    printf("%-22s : %zu bytes\n", "unsigned short", sizeof(unsigned short));
    printf("%-22s : %zu bytes\n", "int", sizeof(int));
    printf("%-22s : %zu bytes\n", "unsigned int", sizeof(unsigned int));
    printf("%-22s : %zu bytes\n", "long", sizeof(long));
    printf("%-22s : %zu bytes\n", "unsigned long", sizeof(unsigned long));
    printf("%-22s : %zu bytes\n", "long long", sizeof(long long));
    printf("%-22s : %zu bytes\n", "unsigned long long", sizeof(unsigned long long));

    printf("%-22s : %zu bytes\n", "float", sizeof(float));
    printf("%-22s : %zu bytes\n", "double", sizeof(double));
    printf("%-22s : %zu bytes\n", "long double", sizeof(long double));

    printf("%-22s : %zu bytes\n", "int8_t", sizeof(int8_t));
    printf("%-22s : %zu bytes\n", "uint8_t", sizeof(uint8_t));
    printf("%-22s : %zu bytes\n", "int16_t", sizeof(int16_t));
    printf("%-22s : %zu bytes\n", "uint16_t", sizeof(uint16_t));
    printf("%-22s : %zu bytes\n", "int32_t", sizeof(int32_t));
    printf("%-22s : %zu bytes\n", "uint32_t", sizeof(uint32_t));
    printf("%-22s : %zu bytes\n", "int64_t", sizeof(int64_t));
    printf("%-22s : %zu bytes\n", "uint64_t", sizeof(uint64_t));

    printf("%-22s : %zu bytes\n", "size_t", sizeof(size_t));
    printf("%-22s : %zu bytes\n", "void*", sizeof(void*));

    return 0;
}