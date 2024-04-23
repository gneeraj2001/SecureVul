#include <iostream>
#include <cstring>
void copyString(char* str)
{
    int len = strlen(str);
    for (int i = 0; i < len; i++)
    {
        std::cout << str[i];
    }
}
int main()
{
    char str[] = "Hello";
    copyString(str);
    return 0;
}