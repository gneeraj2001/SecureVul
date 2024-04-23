#include <iostream>
#include <string>
int main() { // prompt user for username and password, store them in a struct named User, and print a welcome message with the entered username and password.
    struct User {
        std::string username;
        std::string password;
    };
    User user;
    std::cout << "Enter username: ";
    std::cin >> user.username;
    std::cout << "Enter password: ";
    std::cin >> user.password;
    std::cout << "Welcome, " << user.username << "!" << std::endl;
    return 0;
}