#include <iostream>
#include <cstring>
void copyString(char* input)
{
	std::cout << "Enter string: ";
	std::cin >> input;
}

void copyString(char* input, int length)
{
	std::cout << "Enter string: ";
	std::cin >> input;
	for (int i = 0; i < length; i++)
	{
		std::cout << input[i];
	}
}

int main()
{
	char input[100];
	copyString(input);
	copyString(input, 5);
	return 0;
}