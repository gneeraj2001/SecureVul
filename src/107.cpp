#include <iostream>
#include <cstring>
void copyData(char* input)
{
    int i;
    for(i=0;input[i]!='\0';i++)
    {
        std::cout<<input[i];
    }
    std::cout<<std::endl;
}
int main()
{
    char input[100];
    std::cout<<"Enter the string: ";
    std::cin>>input;
    copyData(input);
    return 0;
}